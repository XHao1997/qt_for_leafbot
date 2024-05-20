from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QGraphicsScene
from LeafBot_ui import Ui_LeafBotForm
from PySide6.QtGui import QPixmap,QImage
from PySide6.QtCore import QTimer, Qt
import qimage2ndarray
import time
from camera_capture import Camera

"""
Camera类只负责从摄像头获取图像
对图像的处理（包括显示）由外部定义
"""

class LeafBot(QWidget, Ui_LeafBotForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.camera = Camera()
        self.timer = QTimer()
        self.timer.timeout.connect(self.showRgb)

        self.timer.start(10)
        self.show_img_width = self.graphicsView.width()
        self.show_img_height = self.graphicsView.height()
        print(self.show_img_width)
        print(self.show_img_height)



    def showRgb(self):
        image = self.camera.capture()
        scene = QGraphicsScene(self)
        image = QImage(image, image.shape[1], image.shape[0], 
                       image.strides[0], QImage.Format_RGB888)
        image = QPixmap.fromImage(image)
        image_scaled = QPixmap.scaled(image, self.show_img_width,self.show_img_height,Qt.IgnoreAspectRatio)
        scene.addPixmap(image_scaled)
        self.graphicsView.setScene(scene)


if __name__ == '__main__':
    app = QApplication([])
    window = LeafBot()
    window.show()
    app.exec()
