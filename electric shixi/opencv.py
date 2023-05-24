import cv2
import numpy as np
import argparse
import imutils
from collections import deque

img = cv2.imread('/home/pi/Pictures/test.png',0)
ret , thred = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thred,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
center = None
if len(contours) > 0:
    c = max(contours, key=cv2.contourArea)
    ((x,y),radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
    if radius > 10:
        cv2.circle(img,(int(x),int(y)),int(radius),(0,255,255),2)
        cv2.circle(img,center,5,(0,0,255),-1)
cv2.imshow("img",img)
key = cv2.waitKey(1) & 0xFF
if key == ord("q"):
    cv2.destroyAllWindows()

