import serial
import threading
import time
from imutils.video import VideoStream
from pyzbar import pyzbar
import datetime
import imutils
import cv2

found = None
is_running = True
class SerialConnection:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.serial = None
        self.receive_message = None
        self.lock = threading.Lock()

    def open(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate)
            if self.serial.isOpen():
                print("Serial port is open")
        except serial.SerialException as e:
            print("Failed to open serial port: ", str(e))
            self.serial = None
        return self.serial is not None

    def close(self):
        if self.serial:
            self.serial.close()
        if not self.serial.isOpen():
            print("Serial port is closed")

    def send(self, message):
        if self.serial:
            try:
                self.serial.write(message.encode('gb2312'))
                return True
            except serial.SerialException as e:
                print("Failed to send message: ", str(e))
        return False

    def receive(self):
        if self.serial.isOpen:
            # self.lock.acquire()
            while is_running:
                print("trying receiving")
                try:
                    self.receive_message = self.serial.readline().decode('gb2312').rstrip()
                    print(self.receive_message)
                except serial.SerialException as e:
                    print("Failed to receive message: ", str(e))
                # finally:
                #     self.lock.release()
            print("receive stop")
        return None


def send_message(message):  # 发送消息
    global ser
    if message == "qian":
        ser.send("q")
        print("前进")
    if message == "hou":
        ser.send("h")
        print("后退")
    if message == "zuo":
        ser.send("z")
        print("左转")
    if message == "you":
        ser.send("y")
        print("右转")


def find_QR():
    global vs
    global found

    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} ({})".format(barcodeData, barcodeType)
        if (found == None or found != barcodeData):
            found = barcodeData
            print(text)
            send_message(barcodeData)
    cv2.imshow("Barcode Scanner", frame)


if __name__ == '__main__':
    global ser
    ser = SerialConnection('/dev/ttyAMA0', 115200) #create serial
    ser.open()
    receive_thread = threading.Thread(target=ser.receive) #create receive thread
    receive_thread.start()
    global vs
    vs = VideoStream(src=0).start()  #open camera
    time.sleep(2.0)
    print("[INFO] starting video stream...")
    while True:
        find_QR()
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
    vs.stop()
    is_running = False
    receive_thread.join()
    ser.close()