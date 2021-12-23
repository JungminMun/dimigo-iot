import spidev
import time
import RPi.GPIO as GPIO

# SPI 인스턴스 생성
spi = spidev.SpiDev()

# SPI 통신 시작
spi.open(0, 0) #bus : 0, device  : 0 (CE0, CE1)

# SPI 최대 통신 속도 설정
spi.max_speed_hz = 100000

ledPin = 14
GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
GPIO.setup(ledPin, GPIO.OUT) # GPIO.OUT or GIPo.in

# 채널에서 읽어온 아날로그값을 디지털로 변환하여 리턴하는 함수
def analog_read(channel):
    # [byte_1, byte_2, byte_3]
    # byte_1 : 1
    # byte_2 : channel(0) + 8 = 0000 1000 << 4 -> 1000 0000
    # byte_3 : 0
    ret = spi.xfer2([1, (channel + 8) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        reading = analog_read(0)
        print("Reading=%d" % reading) # 0~1023
        time.sleep(0.5)

        if reading <= 10:
            GPIO.output(ledPin, GPIO.HIGH) # 1
            print("LED ON")
        else :
            GPIO.output(ledPin, GPIO.LOW) # 1
            print("LED OFF")
finally:
    spi.close()
