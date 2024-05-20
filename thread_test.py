import time
import cv2
import queue 
from threading import Thread
from camera_capture import Camera
 
if __name__ == "__main__":
    # 启动 获取摄像头画面的 线程
    cam = Camera()
    while True:
        image = cam.capture()
        cv2.imshow('img', image)
        cv2.waitKey(1)
