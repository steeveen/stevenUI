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
        self.point = QPoint(0, 0)
        self.wu=23
        self.hu=45

        self.setMouseTracking(True)
        # print('init size', self.img.size())
        # print('init unit', self.scaleUnit)
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Image with mouse control')

    def paintEvent(self, e):
        '''
        绘图
        :param e:
        :return:
        '''
        painter = QPainter()
        painter.begin(self)
        self.draw_img(painter)
        painter.end()

    def draw_img(self, painter):
        painter.drawPixmap(self.point, self.scaled_img)
        self.scaleUnit = self.img.size() / 50
        # print('paint',self.scaled_img.size())

    # def mouseDoubleClickEvent(self, QMouseEvent):
        # print('double click')


    def mouseMoveEvent(self, e):  # 重写移动事件
        # print('mouse move',e.pos())
        # print('mouse trach?',self.hasMouseTracking())
        print('move to ',e.localPos().x())
        if self.left_click:
            self._endPos = e.pos() - self._startPos
            self.point = self.point + self._endPos
            self._startPos = e.pos()
            self.repaint()


    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self._startPos = e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = False
        elif e.button() == Qt.RightButton:
            self.point = QPoint(0, 0)
            self.scaled_img = self.img.scaled(self.size())
            self.repaint()


    def wheelEvent(self, e):
        if e.angleDelta().y() > 0:
            # 缩小图片
            if self.scaled_img.width()>self.wu and self.scaled_img.height()>self.hu:

                self.scaled_img = self.img.scaled(self.scaled_img.width()-self.wu, self.scaled_img.height()-self.hu)
                new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() + self.wu)
                new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() + self.hu)
                # print('rescaled:',self.scaled_img.width()-self.wu, self.scaled_img.height()-self.hu )
                self.point = QPoint(new_w, new_h)
                self.repaint()
        elif e.angleDelta().y() < 0:
            # 放大图片
            self.scaled_img = self.img.scaled(self.scaled_img.width()+self.wu, self.scaled_img.height()+self.hu)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() - self.wu)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() - self.hu)
            # print('rescaled:', self.scaled_img.width() - self.wu,
            #       self.scaled_img.height() - self.hu)
            self.point = QPoint(new_w, new_h)
            self.repaint()

    def resizeEvent(self, e):
        if self.parent is not None:
            self.scaled_img = self.img.scaled(self.size())
            self.point = QPoint(0, 0)
            self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    # ex = ImageWithMouseControl()
    ex.show()
    app.exec_()
