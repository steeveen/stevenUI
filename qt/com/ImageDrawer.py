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

class ImageDrawer(ImageShower):
    def __init__(self, parent=None, imagePath=r'E:\pyWorkspace\stevenUI\res\ct.tif',maskPath=r'E:\pyWorkspace\stevenUI\res\pre.bmp'):
        super().__init__(parent,imagePath)
        print(' init imageDrawer')
        self.brushDraw = True
        self.brushSize = 3

        self.alpha=128
        self.maskNp = (skio.imread(maskPath) > 0).astype(np.uint8)
        # self.maskNp[:, :, 3] = 0

        self.maskX = 0
        self.maskY = 0
        # self.

    def updateDrawerSize(self, size):
        self.brushSize = size
        print('size type', type(size))
        print('drawer size', size)

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

    def setMask(self,mask=None):
        # if type(mask)==NoneType:
        #     mask=np.zeros((self.maskNp.shape[0],self.maskNp.shape[1]))
        self.maskNp = (mask>0).astype(np.uint8)
        self.repaint()

    def mouseDragNoCtrl(self, e):
        print('drawer mouse drag')
        # self.prepareMoveMaskCenter(int(e.pos().x()), int(e.pos().y()))
        point=self.mapMouseImgPoint(e.pos())
        self.prepareMaskImg(point.x(),point.y())

    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        if e.button() == Qt.LeftButton and not self.ctrlDown:
            point = self.mapMouseImgPoint(e.pos())
            self.prepareMaskImg(point.x(), point.y())



    def drawMask(self):

        zNp=np.zeros((self.maskNp.shape[0],self.maskNp.shape[1]))
        showMask=np.stack([self.maskNp*255,zNp,zNp,self.maskNp*self.alpha],axis=2)
        self.painter.drawPixmap(self.imgPoint, self.np2QPixmap(showMask).scaled(QSize(*self.showImgScale)))

    def getMask(self):
        return self.maskNp

    def paintEvent(self, QPaintEvent):
        self.painter.begin(self)
        self.drawImg()
        self.drawMask()
        self.drawGuideLine()
        self.painter.end()
