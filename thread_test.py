import time
import cv2
import queue 
from threading import Thread
 
 
"""
Camera类只负责从摄像头获取图像
对图像的处理（包括显示）由外部定义
"""
class Camera:
    def __init__(self, device_id, frame_queue):
        self.device_id = device_id  # 摄像头id
        self.cam = cv2.VideoCapture(self.device_id)  # 获取摄像头
        self.frame_queue = frame_queue  # 帧队列
        self.is_running = False  # 状态标签
        self.fps = 0.0  # 实时帧率
        self._t_last = time.time() * 1000
        self._data = {} 
 
    def capture_queue(self):
        # 捕获图像
        self._t_last = time.time() * 1000
        while self.is_running and self.cam.isOpened():
            ret, frame = self.cam.read()
            if not ret:
                break
            if self.frame_queue.qsize() < 1: 
                # 当队列中的图像都被消耗完后，再压如新的图像              
                t  = time.time() * 1000
                t_span = t - self._t_last                
                self.fps = int(1000.0 / t_span)
                self._data["image"] = frame.copy()
                self._data["fps"] = self.fps
                self.frame_queue.put(self._data)
                self._t_last = t
 
    def run(self):
        self.is_running = True
        self.thread_capture = Thread(target=self.capture_queue)
        self.thread_capture.start()
 
    def stop(self):
        self.is_running = False
        self.cam.release()
 
 
# 对于图像的处理方法
def show_frame(frame):
        while True:
            # 根据实际需求，设置跳出循环（结束线程）的方法
            data = frame.get()
            image = data["image"]
            cv2.putText(image, "fps:{fps}".format(fps=data["fps"]), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0 ,0))
            cv2.namedWindow("camera", cv2.WINDOW_AUTOSIZE)    
            cv2.imshow("camera", image)
            if cv2.waitKey(1)& 0xFF == ord('q'): 
                break
            frame_queue.task_done()
 
 
if __name__ == "__main__":
    # 启动 获取摄像头画面的 线程
    frame_queue = queue.LifoQueue()
    cam = Camera(0, frame_queue)
    cam.run()
    # 启动处理（显示）摄像头画面的线程
    thread_show = Thread(target=show_frame, args=(frame_queue,))
    thread_show.start()
    time.sleep(60)
    cam.stop()
    # TO DO 修改图像处理的死循环（while True）确保可正常结束。