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
from skimage import io as skio
import  numpy as np
from PyQt5.QtCore import QRect
import qimage2ndarray


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = ImageShower(self)
        self.widget.setGeometry(10, 10, 600, 600)
        self.setWindowTitle('Image with mouse control')


class ImageShower(QWidget):

    def __init__(self, parent=None, imagePath=r'E:\pyWorkspace\stevenUI\res\ct.tif'):
        super().__init__(parent)
        print(' init ')
        self.parent = parent
        self.setMouseTracking(True)

        # self.img = QPixmap(imagePath)#原图
        self.loadImg(imagePath)
        self.scaled_img = self.img.scaled(self.size())#经过放缩后显示的图
        self.__imgPoint = QPoint(0, 0)#图像的起始点，拖拽和放缩的时候用
        self.setScaleUnit(self.width(), self.height())  # 初始化放缩的单位大小

        self.guideLineX=0#引导线X坐标
        self.guideLineY=0#引导线Y坐标
        self.guideLineColor='#88FF34B3'#引导线颜色 ARGB
        self.guideLineThickness=1.5#引导线粗细

        self.painter = QPainter()#绘制引导线、更新显示图所使用的画笔

        self.leftClick = False#左键是否点击了，区分鼠标是拖拽还是滑动时使用
        self.hasLocWatcher = False#位置以及值的监控控件是否已经设置
        self.hasFriendWatcher = False#联动的控件是否已经设置

        # self.v=0用于测试label框中的数值的

        self.initUI()

    def loadImg(self,path):
        imgNp=skio.imread(path)
        print(imgNp.shape)
        print(imgNp.dtype)
        self.img = QPixmap(qimage2ndarray.array2qimage(imgNp))


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

    def setScaleUnit(self,width,height):
        self.wu = width//10
        self.hu = height//10

    def setGeometry(self, *geo):
        if len(geo)==1:
            rect=geo[0]
            self.setScaleUnit(rect.width(),rect.height())
        else:
            # TODO 传入的是四个int值
            pass
        super().setGeometry(*geo)

    def setLocWatcher(self, x, y, v):
        self.hasLocWatcher = True
        self.x = x
        self.y = y
        self.v = v

    def setFriendWatcher(self, showers:List['ImageShower']):
        self.hasFriendWatcher = True
        self.friendsWatchers = showers


    def initUI(self):
        self.setWindowTitle('Image with mouse control')


    def paintEvent(self, QPaintEvent):
        self.painter.begin(self)
        self.drawImg()
        self.drawGuideLine()
        self.painter.end()

    def drawImg(self):
        self.painter.drawPixmap(self.imgPoint, self.scaled_img)

    def drawGuideLine(self):
        self.painter.setPen(QPen(QColor(self.guideLineColor),self.guideLineThickness))
        self.painter.drawLine(QPoint(0, self.guideLineY), QPoint(self.width(), self.guideLineY))
        self.painter.drawLine(QPoint(self.guideLineX, 0), QPoint(self.guideLineX, self.height()))



    def mouseMoveEvent(self, e):  # 重写移动事件
        if self.leftClick:
            pointBias = e.pos() - self._startPos
            self._startPos = e.pos()
            self.prepareMoveImg(pointBias)
            self.prepareMoveFriendWatcherImg(pointBias)
        else:
            self.updateLocWatcher(int(e.pos().x()), int(e.pos().y()))
        self.prepareMoveGuildLine(int(e.pos().x()), int(e.pos().y()))
        self.prepareMoveFriendGuildLine(int(e.pos().x()), int(e.pos().y()))

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.leftClick = True
            self._startPos = e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.leftClick = False
        elif e.button() == Qt.RightButton:
            self.prepareRecoverImg()
            self.prepareRecoverFriendWatcherImg()

    def wheelEvent(self, e):
        if e.angleDelta().y() > 0:
            zoom = -1
        elif e.angleDelta().y() < 0:
            zoom = 1
        self.prepareZoomImg(zoom, e.pos().x(), e.pos().y())
        self.prepareZoomFriendWatcherImg(zoom, e.pos().x(), e.pos().y())


    def prepareRecoverImg(self):
        self.imgPoint = QPoint(0, 0)
        self.scaled_img = self.img.scaled(self.size())
        self.repaint()

    def prepareRecoverFriendWatcherImg(self):
        if self.hasFriendWatcher:
            for shower in self.friendsWatchers:
                shower.prepareRecoverImg()

    def prepareMoveImg(self, pointBias):
        self.imgPoint = self.imgPoint + pointBias
        self.repaint()

    def prepareMoveFriendWatcherImg(self, pointBias):
        if self.hasFriendWatcher:
            for shower in self.friendsWatchers:
                shower.prepareMoveImg(pointBias)

    def prepareZoomImg(self, zoom, x, y):
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
            if self.scaled_img.width() > self.width() \
                    and self.scaled_img.size() != self.size():#当视图比控件大的时候才可以缩小
                self.scaled_img = self.img.scaled(self.scaled_img.width() - self.wu, self.scaled_img.height() - self.hu)
                new_w = x - (self.scaled_img.width() * (x - self.imgPoint.x())) / (
                        self.scaled_img.width() + self.wu)
                new_h = y - (self.scaled_img.height() * (y - self.imgPoint.y())) / (
                        self.scaled_img.height() + self.hu)
                self.imgPoint = QPoint(new_w, new_h)
                self.repaint()

    def prepareZoomFriendWatcherImg(self, zoom, x, y):
        if self.hasFriendWatcher:
            for shower in self.friendsWatchers:
                shower.prepareZoomImg(zoom, x, y)

    def prepareMoveGuildLine(self, mouseX, mouseY):
        self.guideLineX = mouseX
        self.guideLineY = mouseY
        self.repaint()

    def prepareMoveFriendGuildLine(self,mouseX,mouseY):
        if self.hasFriendWatcher:
            for shower in self.friendsWatchers:
                shower.prepareMoveGuildLine(mouseX,mouseY)


    def updateLocWatcher(self, x, y):
        if self.hasLocWatcher:
            self.x.setText(str(x))
            self.y.setText(str(y))
            self.v.setText(str(0))
            # TODO 显示数值


    def resizeEvent(self, e):
        # 设置大小时会调用此函数
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
