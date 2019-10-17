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
import numpy as np
from PyQt5.QtCore import QRect
import qimage2ndarray


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = ImageShower(self)
        self.widget.setGeometry(10, 10, 500, 200)
        self.setWindowTitle('Image with mouse control')


class ImageShower(QWidget):

    def __init__(self, parent=None, imagePath=r'E:\pyWorkspace\stevenUI\res\ct.tif'):
        super().__init__(parent)
        print(' init ')

        self.parent = parent
        self.setMouseTracking(True)

        # self.img = QPixmap(imagePath)#原图

        imgNp = skio.imread(imagePath)
        self.imgNp = np.stack([imgNp, imgNp, imgNp], axis=2)

        self.showImgScale = (self.size().width(), self.size().height())
        self.imgPoint = QPoint(0, 0)  # 图像的起始点，拖拽和放缩的时候用
        self.showMousePos = QPoint(0, 0)

        self.setScaleUnit(self.width(), self.height())  # 初始化放缩的单位大小

        self.guideLineX = 0  # 引导线X坐标
        self.guideLineY = 0  # 引导线Y坐标
        self.guideLineColor = '#88FF34B3'  # 引导线颜色 ARGB
        self.guideLineThickness = 1.5  # 引导线粗细

        self.painter = QPainter()  # 绘制引导线、更新显示图所使用的画笔

        self.leftClick = False  # 左键是否点击了，区分鼠标是拖拽还是滑动时使用
        self.hasLocWatcher = False  # 位置以及值的监控控件是否已经设置
        self.hasFriendWatcher = False  # 联动的控件是否已经设置

        self.ctrlDown = False

        self.initUI()

    # def mapMouseRealPoint(self, pos):
    #     '''
    #     将鼠标在视图中的位置映射为放大后图像中的位置
    #     :param pos: 鼠标位置
    #     :return: 映射后在放大的图像上的位置（左上角为0,0，第一维为x，第二维为y）
    #     '''
    #     print('-----------------')
    #     print('img scale', self.showImgScale)
    #     print('size', self.size())
    #     print('img pint', self.imgPoint)
    #     print('-----------------')
    #     realX = pos.x() * self.showImgScale[0] / self.size().width() - self.imgPoint.x()
    #     realY = pos.y() * self.showImgScale[1] / self.size().height() - self.imgPoint.y()
    #     self.showMousePos = QPoint(int(realX), int(realY))
    #     return self.showMousePos

    def np2QPixmap(self,arr):
        return QPixmap(qimage2ndarray.array2qimage(arr))

    def mapMouseImgPoint(self, pos):
        '''
        将鼠标在视图中的位置映射为图像矩阵中的位置
        :param pos: 鼠标位置
        :return: 映射后在放大的图像上的位置（左上角为0,0，第一维为x，第二维为y），与矩阵的正好反过来
        '''

        imgX = int(self.imgNp.shape[1] / self.showImgScale[0] * (pos.x() - self.imgPoint.x()))
        imgY = int(self.imgNp.shape[0] / self.showImgScale[1] * (
                pos.y() - self.imgPoint.y()))
        # print('bias y', self.imgPoint.y())
        # print('scale y', self.showImgScale[1])
        return QPoint(int(imgX), int(imgY))





    @property
    def imgPoint(self):
        return self.__imgPoint

    @imgPoint.setter
    def imgPoint(self, newImgPoint: QPoint):
        maxX = 0
        minX = self.width() - self.showImgScale[0]
        maxY = 0
        minY = self.height() - self.showImgScale[1]
        self.__imgPoint = QPoint(max(min(maxX, newImgPoint.x()), minX), max(min(maxY, newImgPoint.y()), minY))

    def setScaleUnit(self, width, height):
        self.wu = width // 10
        self.hu = height // 10

    def setGeometry(self, *geo):
        super().setGeometry(*geo)
        if len(geo) == 1:
            rect = geo[0]
            self.setScaleUnit(rect.width(), rect.height())
        else:
            # TODO 传入的是四个int值
            pass
        self.showImgScale = (self.size().width(), self.size().height())

    def setLocWatcher(self, x, y, v):
        self.hasLocWatcher = True
        self.x = x
        self.y = y
        self.v = v

    def setFriendWatcher(self, showers: List['ImageShower']):
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
        self.painter.drawPixmap(self.imgPoint,self.np2QPixmap(self.imgNp).scaled(QSize(*self.showImgScale)))

    def drawGuideLine(self):
        self.painter.setPen(QPen(QColor(self.guideLineColor), self.guideLineThickness))
        self.painter.drawLine(QPoint(0, self.guideLineY), QPoint(self.width(), self.guideLineY))
        self.painter.drawLine(QPoint(self.guideLineX, 0), QPoint(self.guideLineX, self.height()))

    def enterEvent(self, QEvent):
        self.grabKeyboard()

    def leaveEvent(self, QEvent):
        self.releaseKeyboard()

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ControlModifier:
            self.ctrlDown = True
        print('press ctrl', self.ctrlDown)

    def keyReleaseEvent(self, event):
        if event.modifiers() != Qt.ControlModifier:
            self.ctrlDown = False
        print('release ctrl', self.ctrlDown)

    def mouseDragNoCtrl(self, e):
        '''
        不按ctrl的操作，子类可以继承
        :param e:
        :return:
        '''
        print('mouse move no ctrl', e)

    def mouseMoveEvent(self, e):  # 重写移动事件
        if self.leftClick:
            if self.ctrlDown:  # 按下ctrl同时拖拽鼠标表示移动
                pointBias = e.pos() - self._startPos
                self._startPos = e.pos()
                self.prepareMoveImg(pointBias)
                self.prepareMoveFriendWatcherImg(pointBias)
            else:
                self.mouseDragNoCtrl(e)  # 只移动鼠标，没有按下ctrl键
        else:
            self.updateLocWatcher(int(e.pos().x()), int(e.pos().y()), )
            mouseImgPoint = self.mapMouseImgPoint(e.pos())
            self.updateLocValueWatcher(mouseImgPoint)
            self.updateFriendLocValueWatcher(mouseImgPoint)
        self.prepareMoveGuildLine(int(e.pos().x()), int(e.pos().y()))
        self.prepareMoveFriendGuildLine(int(e.pos().x()), int(e.pos().y()))

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            print('imgNp shape', self.imgNp.shape)
            print(self.mapMouseImgPoint(e.pos()))
            self.leftClick = True
            self._startPos = e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.leftClick = False
        elif e.button() == Qt.RightButton:
            self.prepareRecoverImg()
            self.prepareRecoverFriendWatcherImg()

    def wheelEvent(self, e):
        # print(self.imgPoint.x())
        # print(self.showImgScale)
        if e.angleDelta().y() > 0:
            zoom = -1
        elif e.angleDelta().y() < 0:
            zoom = 1
        self.prepareZoomImg(zoom, e.pos().x(), e.pos().y())
        self.prepareZoomFriendWatcherImg(zoom, e.pos().x(), e.pos().y())

    def prepareRecoverImg(self):
        self.imgPoint = QPoint(0, 0)
        self.showImgScale=(self.size().width(),self.size().height())
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
            self.showImgScale = (self.showImgScale[0]+ self.wu, self.showImgScale[1] + self.hu)

            new_w = x - (self.showImgScale[0] * (x - self.imgPoint.x())) / (
                    self.showImgScale[0] - self.wu)
            new_h = y - (self.showImgScale[1] * (y - self.imgPoint.y())) / (
                    self.showImgScale[1] - self.hu)
            self.imgPoint = QPoint(new_w, new_h)
            self.repaint()
        elif zoom < 0:
            # 缩小图片
            if self.showImgScale[0] > self.width() \
                    and QSize(*self.showImgScale) != self.size():  # 当视图比控件大的时候才可以缩小
                self.showImgScale = (self.showImgScale[0] - self.wu, self.showImgScale[1] - self.hu)

                new_w = x - (self.showImgScale[0] * (x - self.imgPoint.x())) / (
                        self.showImgScale[0] + self.wu)
                new_h = y - (self.showImgScale[1] * (y - self.imgPoint.y())) / (
                        self.showImgScale[1] + self.hu)
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

    def prepareMoveFriendGuildLine(self, mouseX, mouseY):
        if self.hasFriendWatcher:
            for shower in self.friendsWatchers:
                shower.prepareMoveGuildLine(mouseX, mouseY)

    def updateLocValueWatcher(self, mouseImgPoint):
        if self.hasLocWatcher:
            self.v.setText(str(int(self.imgNp[mouseImgPoint.y(), mouseImgPoint.x(),0])))

    def updateFriendLocValueWatcher(self, mouseImgPoint):
        if self.hasFriendWatcher:
            for friend in self.friendsWatchers:
                friend.updateLocValueWatcher(mouseImgPoint)

    def updateLocWatcher(self, x, y):
        if self.hasLocWatcher:
            self.x.setText(str(x))
            self.y.setText(str(y))
            # TODO 显示数值

    def resizeEvent(self, e):
        # 设置大小时会调用此函数
        if self.parent is not None:
            self.showImgScale=(self.size().width(),self.size().height())
            self.imgPoint = QPoint(0, 0)
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    # ex = ImageWithMouseControl()
    ex.show()
    app.exec_()
