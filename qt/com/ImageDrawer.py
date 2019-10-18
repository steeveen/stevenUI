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
 @Belong = 'newStevenUi'  @MadeBy = 'PyCharm'
 @Author = 'steven'   @DateTime = '2019/10/15 13:52'
'''
import qimage2ndarray

from .ImageShower import ImageShower, QPen, QPainter, Qt, QBrush, QRect, QPixmap, QSize
import numpy as np
from skimage import  draw as skd
from skimage import io as skio
from .ImageMaskShower import ImageMaskShower
class ImageDrawer(ImageMaskShower):
    def __init__(self, parent, image,mask):
        super().__init__(parent,image,mask)
        self.brushDraw = 0
        self.brushSize = 3

    def updateDrawerSize(self, size):
        self.brushSize = size

    def updateDrawerMode(self, draw):
        if draw == 1:
            print('切换为添加模式')
        elif draw == -1:
            print('切换为删除模式')
        else:
            print('切换为关闭模式')
        self.brushDraw = draw

    def prepareMaskImg(self,mouseX, mouseY):
        cc, rr = skd.circle(mouseX, mouseY, self.brushSize/2)
        if self.brushDraw==1:
            skd.set_color(self.maskNp, [rr, cc], 1)
        elif self.brushDraw==-1:
            skd.set_color(self.maskNp, [rr, cc],0)
        self.repaint()

    def setOriMaskNp(self, maskNp):
        self.maskNp = maskNp
        self.repaint()

    def mouseDragNoCtrl(self, e):
        print('drawer mouse drag')
        point=self.mapMouseImgPoint(e.pos())
        self.prepareMaskImg(point.x(),point.y())

    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        if e.button() == Qt.LeftButton and not self.ctrlDown:
            point = self.mapMouseImgPoint(e.pos())
            self.prepareMaskImg(point.x(), point.y())



