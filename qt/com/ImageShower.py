# -*- coding: utf-8 -*-
'''
        司马懿：“善败能忍，然厚积薄发”
                                    ——李叔说的
code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
          --┃      ☃      ┃--
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗II━II┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
 @Belong = 'stevenUI'  @MadeBy = 'PyCharm'
 @Author = 'steven'   @DateTime = '2019/7/9 20:48'
'''
# encoding:utf8

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = ImageShower(self)
        self.widget.setGeometry(10, 10, 600, 600)
        self.setWindowTitle('Image with mouse control')


class ImageShower(QWidget):

    def __init__(self, parent=None,imagePath=r'E:\pyWorkspace\stevenUI\res\ct.tif'):
        super().__init__(parent)
        self.parent = parent
        self.img = QPixmap(imagePath)
        self.scaled_img = self.img.scaled(self.size())
        self.__imgPoint = QPoint(0, 0)
        self.wu=23
        self.hu=45
        self.left_click=False
        self.hasWatcher=False
        self.setMouseTracking(True)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image with mouse control')

    def setLocWatcher(self,x,y,v):
        self.hasWatcher=True
        self.x=x
        self.y=y
        self.v=v

    def paintEvent(self, QPaintEvent):
        self.draw_img()

    def draw_img(self):
        painter = QPainter()
        painter.begin(self)
        painter.drawPixmap(self.imgPoint, self.scaled_img)
        painter.end()

    @property
    def imgPoint(self):
        return self.__imgPoint

    @imgPoint.setter
    def imgPoint(self,newImgPoint:QPoint):
        maxX=0
        minX=self.width()-self.scaled_img.width()
        maxY=0
        minY=self.height()-self.scaled_img.height()
        qp=QPoint(max(min(maxX,newImgPoint.x()),minX),max(min(maxY,newImgPoint.y()),minY))
        self.__imgPoint=qp

        print(self.__imgPoint)
        print(self.__imgPoint)

    def mouseMoveEvent(self, e):  # 重写移动事件

        if self.left_click:
            self.pointBias = e.pos() - self._startPos
            self._startPos = e.pos()
            self.imgPoint = self.imgPoint + self.pointBias

            self.repaint()
        else:
            if self.hasWatcher:
                self.x.setText('good')
                self.x.setText(str(int(e.localPos().x())))
                self.y.setText(str(int(e.localPos().y())))

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self._startPos = e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = False
        elif e.button() == Qt.RightButton:
            self.recoverImg()
    def recoverImg(self):
        self.imgPoint = QPoint(0, 0)
        self.scaled_img = self.img.scaled(self.size())
        self.repaint()

    def wheelEvent(self, e):
        if e.angleDelta().y() > 0:
            # 缩小图片
            if self.scaled_img.width()>self.width() and self.scaled_img.height()>self.height():
                self.scaled_img = self.img.scaled(self.scaled_img.width()-self.wu, self.scaled_img.height()-self.hu)
                new_w = e.x() - (self.scaled_img.width() * (e.x() - self.imgPoint.x())) / (self.scaled_img.width() + self.wu)
                new_h = e.y() - (self.scaled_img.height() * (e.y() - self.imgPoint.y())) / (self.scaled_img.height() + self.hu)
                if self.scaled_img.size()==self.size():
                    self.recoverImg()
                else:
                    self.imgPoint = QPoint(new_w, new_h)
                    self.repaint()
        elif e.angleDelta().y() < 0:
            # 放大图片
            self.scaled_img = self.img.scaled(self.scaled_img.width()+self.wu, self.scaled_img.height()+self.hu)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.imgPoint.x())) / (self.scaled_img.width() - self.wu)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.imgPoint.y())) / (self.scaled_img.height() - self.hu)

            self.imgPoint = QPoint(new_w, new_h)
            self.repaint()

    def resizeEvent(self, e):
        if self.parent is not None:
            self.scaled_img = self.img.scaled(self.size())
            self.imgPoint = QPoint(0, 0)
            self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    # ex = ImageWithMouseControl()
    ex.show()
    app.exec_()
