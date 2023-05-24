import PCF8591 as ADC
import RPi.GPIO as GPIO
import math
import time

makerobo_test = 11
GPIO.setmode(GPIO.BOARD)  # 采用实际的物理管脚给GPIO口

def makerobo_setup():
    GPIO.setup(makerobo_test, GPIO.OUT)
    GPIO.output(makerobo_test, GPIO.HIGH)

def loop():
    GPIO.output(makerobo_test, GPIO.LOW)
    time.sleep(100)
    GPIO.output(makerobo_test, GPIO.HIGH)

if __name__ == '__main__':
    makerobo_setup()
    loop()
