import PCF8591 as ADC
import RPi.GPIO as GPIO
import math
import time

makerobo_led_pin = 11      #声控灯输出管脚
makerobo_sound_pin = 12    #声音传感器输入管脚
makerobo_fire_pin = 13    #火灾灯输出管脚
makerobo_Buzzer_pin = 15  #火灾报警器输出管脚
time_counter = 5          #时间计数器
GPIO.setmode(GPIO.BOARD)        #采用实际的物理管脚给GPIO口


def makerobo_setup():     #初始化函数
    ADC.setup(0x48)       #设置8591地址
    #设置GPIO口输入输出模式
    GPIO.setup(makerobo_led_pin, GPIO.OUT)
    GPIO.setup(makerobo_sound_pin, GPIO.IN)
    GPIO.setup(makerobo_fire_pin, GPIO.OUT)
    GPIO.setup(makerobo_Buzzer_pin, GPIO.OUT)
    GPIO.output(makerobo_led_pin, GPIO.LOW)
    GPIO.output(makerobo_fire_pin, GPIO.LOW)
    GPIO.output(makerobo_Buzzer_pin, GPIO.HIGH)



def makerobo_loop():        #循环函数
    light = ADC.read(0)     #读入8591的光敏电阻的值
    tempareture = change(ADC.read(1))       #读入模拟温度传感器的值并转化为摄氏度

    #打印相关信息
    print('light = ', light)        
    print('temperature = ', tempareture, 'C')
    print('sound = ', GPIO.input(makerobo_sound_pin))

    global time_counter   #time_counter是为了能够时刻进行火灾预警而设的全局变量（避免使用time.sleep） 
    time_counter += 0.2

    if light > 100 and tempareture < 50 and time_counter >= 5:   #当光线足够暗且并非火灾时，控制声控灯的开关，time_counter使声控灯打开至少5s再进行下一次判断
        if GPIO.input(makerobo_sound_pin) == GPIO.LOW:          #判断有无声音
            GPIO.output(makerobo_led_pin, GPIO.HIGH)
            time_counter = 0                                  #重置time_counter
        else:
            GPIO.output(makerobo_led_pin, GPIO.LOW)
    elif light < 100 and tempareture < 50:
        GPIO.output(makerobo_led_pin, GPIO.LOW)

    
    if tempareture > 50 and light > 150:                                   #如果温度和光线（烟雾浓度）超过预警，警报灯亮红灯，声控灯常亮，蜂鸣器工作
        GPIO.output(makerobo_led_pin, GPIO.HIGH)
        GPIO.output(makerobo_fire_pin, GPIO.HIGH)
        makerobo_beep(0.5)
    else:
        GPIO.output(makerobo_fire_pin, GPIO.LOW)
        GPIO.output(makerobo_Buzzer_pin, GPIO.HIGH)


def change(makerobo_analogVal):          #将温度传感器的值转化为摄氏度
    makerobo_Vr = 5 * float(makerobo_analogVal) / 255
    makerobo_Rt = 10000 * makerobo_Vr / (5 - makerobo_Vr)
    makerobo_temp = 1 / (((math.log(makerobo_Rt / 10000)) / 3950) + (1 / (273.15 + 25)))
    makerobo_temp = makerobo_temp - 273.15
    return makerobo_temp

def makerobo_buzzer_on():
    GPIO.output(makerobo_Buzzer_pin, GPIO.LOW)

def makerobo_buzzer_off():
    GPIO.output(makerobo_Buzzer_pin, GPIO.HIGH)

def makerobo_beep(x):    #蜂鸣器工作函数
    makerobo_buzzer_on()
    time.sleep(x)
    makerobo_buzzer_off()
    time.sleep(x)

def makerobo_set_white():


def destroy():
    GPIO.output(makerobo_led_pin, GPIO.LOW)
    GPIO.cleanup()
    ADC.write(0)


if __name__ == '__main__':
    try:
        makerobo_setup()
        while True:
            makerobo_loop()
            time.sleep(0.5)
    except KeyboardInterrupt:
        destroy()
