import cv2
import numpy as np
import argparse
from collections import deque
import imutils
import time
import RPi.GPIO as GPIO

makerobo_R = 11      #灯红输出管脚
makerobo_G = 12      #灯绿输出管脚
makerobo_B = 13      #灯蓝输出管脚
GPIO.setmode(GPIO.BOARD)        #采用实际的物理管脚给GPIO口
GPIO.setwarnings(False)
GPIO.setup(makerobo_R,GPIO.OUT)
GPIO.setup(makerobo_G,GPIO.OUT)
GPIO.setup(makerobo_B,GPIO.OUT)
GPIO.output(makerobo_R,GPIO.LOW)
GPIO.output(makerobo_G,GPIO.LOW)
GPIO.output(makerobo_B,GPIO.LOW)
p_R = GPIO.PWM(makerobo_R, 2000)
p_G = GPIO.PWM(makerobo_G, 1999)
p_B = GPIO.PWM(makerobo_B, 5000)
p_R.start(0)
p_G.start(0)
p_B.start(0)


vs = cv2.VideoCapture(0)
while True:
    (grabbed,frame) = vs.read()
    imgContour = frame.copy()
    imggray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imggray,(7,7),1)
    imgCanny = cv2.Canny(imgBlur,50,50)
    contours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            cv2.polylines(imgContour,[approx],True,(0,0,255),2)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            if objCor == 3:
                objectType = "Tri"
                cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                p_R.ChangeDutyCycle(100)
                p_G.ChangeDutyCycle(0)
                p_B.ChangeDutyCycle(0)
                print(objectType)
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio >0.95 and aspRatio <1.05:
                    objectType = "Square"
                    cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                    p_R.ChangeDutyCycle(100)
                    p_G.ChangeDutyCycle(100)
                    p_B.ChangeDutyCycle(0)
                    print(objectType)
                else:
                    objectType = "Rectangle"
                    cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                    p_R.ChangeDutyCycle(0)
                    p_G.ChangeDutyCycle(100)
                    p_B.ChangeDutyCycle(0)
                    print(objectType)
            elif objCor >4:
                objectType = "Circle"
                cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                p_R.ChangeDutyCycle(0)
                p_G.ChangeDutyCycle(0)
                p_B.ChangeDutyCycle(100)
                print(objectType)
    if len(contours) <= 0:
        print("None")
        GPIO.output(makerobo_B,GPIO.LOW)
        GPIO.output(makerobo_G,GPIO.LOW)
        GPIO.output(makerobo_R,GPIO.LOW)

    cv2.imshow("img",frame)
    cv2.imshow("edge",imgCanny)
    cv2.imshow("shape",imgContour)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

p_B.stop()
p_G.stop()
p_R.stop()
GPIO.cleanup()
cv2.destroyAllWindows()
vs.release()

