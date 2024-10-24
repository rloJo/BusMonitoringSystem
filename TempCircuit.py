# TempCircuit.py
import time
import RPi.GPIO as GPIO
from adafruit_htu21d import HTU21D
import busio

GPIO.setmode(GPIO.BCM) #BCM 모드 설정
GPIO.setwarnings(False)
sda = 2 #GPIO핀번호 sda
scl = 32 #GPIO핀번호 scl
i2c = busio.I2C(scl, sda)
sensor = HTU21D(i2c) # HTU21D 장치를 제어하는 객체 리턴

def getTemp() : #측정한 온도값을 return하는 함수
    return float(sensor.temperature)
