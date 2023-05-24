import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np
import time

# 基于轮廓定位QR位置
def find_code(img):
    # 高斯滤波
    blur = cv2.GaussianBlur(img,(5,5),0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二值化
    ret,th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # 形态学操作
    mask=cv2.erode(th,None,iterations=4)
    mask=cv2.dilate(mask,None,iterations=4)
	# 图像反色
    cv2.bitwise_not(mask, mask)
    # 寻找轮廓
    _,contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	# 寻找QR码的位置
    if len(contours)>0:
        cnt = max(contours, key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(cnt)
        img = cv2.rectangle(img,(x-15,y-15),(x+w+15,y+h+15),(0,255,0),3)
		
        img_ROI = img[y-15:y+h+15, x-15:x+w+15]
     
    else:
        img_ROI = img

    return img_ROI
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
if __name__ == '__main__':
    ret,img = cap.read()
    cv2.imshow("img", img)
    img_ROI = find_code(img)
    scanner = zbar.ImageScanner()
    scanner.parse_config('enable')
    font = cv2.FONT_HERSHEY_SIMPLEX
    img_ROI_gray = cv2.cvtColor(img_ROI, cv2.COLOR_BGR2GRAY)
    width, height = img_ROI_gray.shape  # 获取图片大小
    raw = img_ROI_gray.tobytes()        # 图像矩阵数据转为字节数据
    zarimage = zbar.Image(width, height, 'Y800', raw) # 设置参数
    scanner.scan(zarimage)   # 扫码
	# 解码
    for symbol in zarimage:  
    # do something useful with results 
        if not symbol.count:
            print('decoded', symbol.type, 'symbol', '"%s"' % symbol.data)
        else:
            print('no')
        #cv2.putText(img,symbol.data,(20,100),font,1,(0,255,0),4) # 打印字符在图片上
	# DisPlay
    cv2.imshow('img_ROI', img_ROI_gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        cap.release()

