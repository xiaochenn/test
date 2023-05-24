import PCF8591 as ADC
import RPi.GPIO as GPIO
import math
import time

makerobo_R = 11  # 声控灯红输出管脚
makerobo_G = 12  # 声控灯绿输出管脚
makerobo_B = 13  # 声控灯蓝输出管脚
makerobo_sound_pin = 15  # 声音传感器输入管脚
makerobo_fire_pin = 16  # 火灾灯输出管脚
makerobo_Buzzer_pin = 18  # 火灾报警器输出管脚
time_counter = 5  # 时间计数器
GPIO.setmode(GPIO.BOARD)  # 采用实际的物理管脚给GPIO口


def makerobo_setup():  # 初始化函数
    ADC.setup(0x48)  # 设置8591地址
    global pins
    global p_R, p_G, p_B
    pins = {'pin_R': makerobo_R, 'pin_G': makerobo_G, 'pin_B': makerobo_B}
    # 设置GPIO口输入输出模式
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], GPIO.LOW)
    GPIO.setwarnings(False)
    GPIO.setup(makerobo_sound_pin, GPIO.IN)
    GPIO.setup(makerobo_fire_pin, GPIO.OUT)
    GPIO.setup(makerobo_Buzzer_pin, GPIO.OUT)
    GPIO.output(makerobo_fire_pin, GPIO.LOW)
    GPIO.output(makerobo_Buzzer_pin, GPIO.HIGH)

    #设置pwm调光
    p_R = GPIO.PWM(pins['pin_R'], 2000)
    p_G = GPIO.PWM(pins['pin_G'], 1999)
    p_B = GPIO.PWM(pins['pin_B'], 5000)
    #初始占空比为0
    p_R.start(0)
    p_G.start(0)
    p_B.start(0)


def makerobo_rgb_off():
    #关闭所有灯，不亮
    p_R.ChangeDutyCycle(0)
    p_G.ChangeDutyCycle(0)
    p_B.ChangeDutyCycle(0)

def makerobo_rgb_on():
    #打开所有颜色，全亮，显示为近白光
    p_R.ChangeDutyCycle(50)
    p_G.ChangeDutyCycle(50)
    p_B.ChangeDutyCycle(50)


def makerobo_loop():  # 循环函数
    light = ADC.read(0)  # 读入8591的光敏电阻的值
    tempareture = change(ADC.read(1))  # 读入模拟温度传感器的值并转化为摄氏度

    # 打印相关信息
    print('light = ', light)
    print('temperature = ', tempareture, 'C')
    print('sound = ', GPIO.input(makerobo_sound_pin))

    global time_counter  # time_counter是为了能够时刻进行火灾预警而设的全局变量（避免使用time.sleep）
    time_counter += 0.5

    if light > 100 and tempareture < 50 and time_counter >= 5:  # 当光线足够暗且并非火灾时，控制声控灯的开关，time_counter使声控灯打开至少5s再进行下一次判断
        if GPIO.input(makerobo_sound_pin) == GPIO.LOW:  # 判断有无声音
            makerobo_rgb_on()
            time_counter = 0  # 重置time_counter
        else:
            makerobo_rgb_off()
    elif light < 100 and tempareture < 50:
        makerobo_rgb_off()

    if tempareture > 50 and light > 150:  # 如果温度和光线（烟雾浓度）超过预警，警报灯亮红灯，声控灯常亮，蜂鸣器工作
        makerobo_rgb_on()
        GPIO.output(makerobo_fire_pin, GPIO.HIGH)
        makerobo_beep(0.5)
    else:
        GPIO.output(makerobo_fire_pin, GPIO.LOW)
        GPIO.output(makerobo_Buzzer_pin, GPIO.HIGH)


def change(makerobo_analogVal):  # 将温度传感器的值转化为摄氏度
    makerobo_Vr = 5 * float(makerobo_analogVal) / 255
    makerobo_Rt = 10000 * makerobo_Vr / (5 - makerobo_Vr)
    makerobo_temp = 1 / (((math.log(makerobo_Rt / 10000)) / 3950) + (1 / (273.15 + 25)))
    makerobo_temp = makerobo_temp - 273.15
    return makerobo_temp


def makerobo_buzzer_on():    # 蜂鸣器开关函数
    GPIO.output(makerobo_Buzzer_pin, GPIO.LOW)


def makerobo_buzzer_off():   # 蜂鸣器开关函数
    GPIO.output(makerobo_Buzzer_pin, GPIO.HIGH)


def makerobo_beep(x):  # 蜂鸣器工作函数
    makerobo_buzzer_on()
    time.sleep(x)
    makerobo_buzzer_off()
    time.sleep(x)


def destroy():
    #停止pwm调光
    p_R.stop()
    p_G.stop()
    p_B.stop()
    #关闭rgb灯
    makerobo_rgb_off()
    #释放资源
    GPIO.cleanup()
    ADC.write(0)


if __name__ == '__main__':
    try:
        makerobo_setup() #初始化
        while True:
            makerobo_loop()
            time.sleep(0.5)
    except KeyboardInterrupt:
        destroy()