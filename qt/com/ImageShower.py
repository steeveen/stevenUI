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
from typing import List


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = ImageShower(self)
        self.widget.setGeometry(10, 10, 600, 600)
        self.setWindowTitle('Image with mouse control')


class ImageShower(QWidget):

    def __init__(self, parent=None, imagePath=r'E:\pyWorkspace\stevenUI\res\ct.tif'):
        super().__init__(parent)
        self.parent = parent
        self.img = QPixmap(imagePath)
        self.scaled_img = self.img.scaled(self.size())
        self.__imgPoint = QPoint(0, 0)
        self.wu = 23
        self.hu = 45
        # self.v=0用于测试label框中的数值的
        self.leftClick = False

        self.hasLocWatcher = False
        self.hasFriendWatcher = False

        self.setMouseTracking(True)

        self.initUI()


    def initUI(self):
        self.setWindowTitle('Image with mouse control')

    def setLocWatcher(self, x, y, v):
        self.hasLocWatcher = True
        self.x = x
        self.y = y
        self.v = v

    def setFriendWatcher(self, showers:List['ImageShower']):
        self.hasFriendWatcher = True
        self.friendsWatchers = showers

    def changeFriendWatcher(self):
        if self.hasFriendWatcher:
            # for _shower in self.friendsWatcher:
            #     self.imgPoint=self.imgPoint
            #     self.sca
            pass

    def paintEvent(self, QPaintEvent):
        self.draw_img()

    @property
    def imgPoint(self):
        return self.__imgPoint

    @imgPoint.setter
    def imgPoint(self, newImgPoint: QPoint):
        maxX = 0
        minX = self.width() - self.scaled_img.width()
        maxY = 0
        minY = self.height() - self.scaled_img.height()
        self.__imgPoint = QPoint(max(min(maxX, newImgPoint.x()), minX), max(min(maxY, newImgPoint.y()), minY))

        print(self.__imgPoint)
        print(self.__imgPoint)

    def mouseMoveEvent(self, e):  # 重写移动事件

        if self.leftClick:
            pointBias = e.pos() - self._startPos
            self._startPos = e.pos()
            self.moveImg(pointBias)
            self.moveFriendWatcher(pointBias)
        else:
            self.updateLocWatcher(int(e.pos().x()), int(e.pos().y()))

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.leftClick = True
            self._startPos = e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.leftClick = False
        elif e.button() == Qt.RightButton:
            self.recoverImg()
            self.recoverFriendWatcher()
   
    def wheelEvent(self, e):
        if e.angleDelta().y() > 0:
            zoom = -1
        elif e.angleDelta().y() < 0:
            zoom = 1
        self.rescaleImg(zoom, e.pos().x(), e.pos().y())
        self.rescaleFriendWather(zoom, e.pos().x(), e.pos().y())



    def resizeEvent(self, e):
        # 设置大小时会调用此函数
        if self.parent is not None:
            self.scaled_img = self.img.scaled(self.size())
            self.imgPoint = QPoint(0, 0)
            self.update()

    def draw_img(self):
        painter = QPainter()
        painter.begin(self)
        painter.drawPixmap(self.imgPoint, self.scaled_img)
        painter.end()

    def recoverImg(self):
        self.imgPoint = QPoint(0, 0)
        self.scaled_img = self.img.scaled(self.size())
        self.repaint()

    def moveImg(self, pointBias):
        self.imgPoint = self.imgPoint + pointBias
        self.repaint()

    def rescaleImg(self, zoom, x, y):
        if zoom > 0:  # 放大图片
            self.scaled_img = self.img.scaled(self.scaled_img.width() + self.wu, self.scaled_img.height() + self.hu)
            new_w = x - (self.scaled_img.width() * (x - self.imgPoint.x())) / (
                    self.scaled_img.width() - self.wu)
            new_h = y - (self.scaled_img.height() * (y - self.imgPoint.y())) / (
                    self.scaled_img.height() - self.hu)

            self.imgPoint = QPoint(new_w, new_h)
            self.repaint()
        elif zoom < 0:
            # 缩小图片
            if self.scaled_img.width() > self.width() and self.scaled_img.height() > self.height():
                self.scaled_img = self.img.scaled(self.scaled_img.width() - self.wu, self.scaled_img.height() - self.hu)
                new_w = x - (self.scaled_img.width() * (x - self.imgPoint.x())) / (
                        self.scaled_img.width() + self.wu)
                new_h = y - (self.scaled_img.height() * (y - self.imgPoint.y())) / (
                        self.scaled_img.height() + self.hu)
                if self.scaled_img.size() == self.size():
                    self.recoverImg()
                else:
                    self.imgPoint = QPoint(new_w, new_h)
                    self.repaint()

    def updateLocWatcher(self, x, y):
        if self.hasLocWatcher:
            self.x.setText(str(x))
            self.y.setText(str(y))
            self.v.setText(str(0))
            # TODO 显示数值

    def rescaleFriendWather(self,zoom,x,y):
        if self.hasFriendWatcher:
            for shower in self.friendsWatchers:
                shower.rescaleImg(zoom,x,y)
    def moveFriendWatcher(self,pointBias):
        if self.hasFriendWatcher:
            for shower in self.friendsWatchers:
                shower.moveImg(pointBias)
    def recoverFriendWatcher(self):
        if self.hasFriendWatcher:
            for shower in self.friendsWatchers:
                shower.imgPoint=QPoint(0,0)
                shower.scaled_img=shower.img.scaled(shower.size())
                shower.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    # ex = ImageWithMouseControl()
    ex.show()
    app.exec_()
