# OffCircuit.py
import time
import RPi.GPIO as GPIO
from Passenger import passenger #passenger class 임포트
# 초음파 센서를 대한 전역 변수 선언 및 초기화
trig = 23 #trig는 23번 핀
echo = 24 #echo는 24번 핀

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)

Passenger=passenger()

def measureDistance(): #거리를 측정하는 함수
    time.sleep(0.5)
    global trig, echo
    GPIO.output(trig, True) 
    time.sleep(0.00001)
    GPIO.output(trig, False) 
    while(GPIO.input(echo) == 0):
        pass
    pulse_start = time.time() 
    while(GPIO.input(echo) == 1):
        pass
    pulse_end = time.time() 
    pulse_duration = pulse_end - pulse_start
    return 340*100/2*pulse_duration