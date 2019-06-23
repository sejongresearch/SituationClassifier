import cv2
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtMultimedia
from PyQt5 import QtMultimediaWidgets

body_classifier =  cv2.CascadeClassifier('haarcascade_fullbody.xml')
face_classifier =  cv2.CascadeClassifier('haarcascade_frontface.xml')
class ShowVideo(QtCore.QObject):

    flag = 0

    camera = cv2.VideoCapture('D:/Downloads/road.avi')
    camera1 = cv2.VideoCapture('D:/Downloads/object.avi')
    camera2 = cv2.VideoCapture('D:/Downloads/depth.avi')
    camera3 = cv2.VideoCapture('D:/Downloads/full.avi')
    


    ret, image = camera.read()
    ret1, image1 = camera1.read()
    ret2, image2 = camera2.read()
    ret3, image3 = camera3.read()
    
    height, width = image.shape[:2]
    height1, width1 = image1.shape[:2]
    height2, width2 = image.shape[:2]
    height3, width3 = image.shape[:2]

    VideoSignal1 = QtCore.pyqtSignal(QtGui.QImage)
    VideoSignal2 = QtCore.pyqtSignal(QtGui.QImage)
    VideoSignal3 = QtCore.pyqtSignal(QtGui.QImage)
    VideoSignal4 = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, parent=None):
        super(ShowVideo, self).__init__(parent)   
    

    #QtCore.pyqtSlot()
    def startVideo(self):
        global image
        global image1
        global image2
        global image3

        run_video = True
        while run_video:
            ret, image = self.camera.read()
            ret1, image1 = self.camera1.read()
            ret2, image2 = self.camera.read()
            ret3, image3 = self.camera.read()
            filename = 'translate_tts (4).mp3'
            fullpath = QtCore.QDir.current().absoluteFilePath(filename) 
            media = QtCore.QUrl.fromLocalFile(fullpath)
            content = QtMultimedia.QMediaContent(media)
            player = QtMultimedia.QMediaPlayer()
            player.setMedia(content)

            
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            color_swapped_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
            color_swapped_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
            color_swapped_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)

            
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            bodies= body_classifier.detectMultiScale(gray,1.2,3)
            faces=face_classifier.detectMultiScale(gray,1.2,3)
        
            qt_image1 = QtGui.QImage(color_swapped_image.data,
                                    self.width,
                                    self.height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            self.VideoSignal1.emit(qt_image1)

            qt_image2 = QtGui.QImage(color_swapped_image1.data,
                                    self.width1,
                                    self.height1,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            self.VideoSignal2.emit(qt_image2)

            
            qt_image3 = QtGui.QImage(color_swapped_image2.data,
                                    self.width2,
                                    self.height2,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            self.VideoSignal3.emit(qt_image3)

            
            qt_image4 = QtGui.QImage(color_swapped_image3.data,
                                    self.width3,
                                    self.height3,
                                    color_swapped_image1.strides[0],
                                    QtGui.QImage.Format_RGB888)
            
            self.VideoSignal4.emit(qt_image4)


            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(100, loop.quit) #25 ms
            loop.exec_()

    #QtCore.pyqtSlot()
    def canny(self):
        self.flag = 1 - self.flag


class ImageViewer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()         
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    def initUI(self):
        self.setWindowTitle('Test')

    #QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    thread = QtCore.QThread()
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)

    image_viewer1 = ImageViewer()
    image_viewer2 = ImageViewer()
    image_viewer3 = ImageViewer()
    image_viewer4 = ImageViewer()

    vid.VideoSignal1.connect(image_viewer1.setImage)
    vid.VideoSignal2.connect(image_viewer2.setImage)
    vid.VideoSignal3.connect(image_viewer3.setImage)
    vid.VideoSignal4.connect(image_viewer4.setImage)

    push_button1 = QtWidgets.QPushButton('click')

    push_button1.clicked.connect(vid.startVideo)
    push_button1.clicked.connect(vid.canny)
    
    
    vertical_layout = QtWidgets.QVBoxLayout()
    horizontal_layout = QtWidgets.QHBoxLayout()
   
    horizontal_layout.addWidget(image_viewer1)
    horizontal_layout.addWidget(image_viewer2)
    horizontal_layout.addWidget(image_viewer3)
    
    vertical_layout.addLayout(horizontal_layout)
    vertical_layout.addWidget(image_viewer4)
    
    vertical_layout.addWidget(push_button1)

    #vertical_layout.addWidget(push_button2)

    layout_widget = QtWidgets.QWidget()
    layout_widget.setLayout(vertical_layout)

    main_window = QtWidgets.QMainWindow()
    main_window.setCentralWidget(layout_widget)
    main_window.show()
    sys.exit(app.exec_())
#https://webnautes.tistory.com/1290
