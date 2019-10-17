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

from .ImageShower import ImageShower, QPen, QPainter, Qt, QBrush, QRect, QPixmap
import numpy as np
class ImageDrawer(ImageShower):
    def __init__(self,parent=None, imagePath=r'E:\pyWorkspace\stevenUI\res\ct.tif'):
        super().__init__(parent)
        print(' init imageDrawer')
        self.brushDraw=True
        self.brushSize=3
        self.mask=np.zeros(self.imgNp.shape)

        self.maskX=0
        self.maskY=0
        # self.

    def updateDrawerSize(self,size):
        self.brushSize=size
        print('size type',type(size))
        print('drawer size',size)

    def updateDrawerMode(self,draw):
        if draw==1:
            print('切换为添加模式')
        elif draw==-1:
            print('切换为删除模式')
        else:
            print('切换为关闭模式')
        self.brushDraw=draw

    def prepareMoveMaskCenter(self, mouseX, mouseY):
        self.maskX = mouseX
        self.maskY = mouseY
        print('maskx',self.maskX)
        print('masky',self.maskY)
        self.repaint()

    def mouseDragNoCtrl(self, e):
        print('drawer mouse drag')
        self.prepareMoveMaskCenter(int(e.pos().x()), int(e.pos().y()))
        # print('rrrrrrrrrrrua')
        # qp=QPainter(self)
        # qp.setPen(QPen())
        # qp.setBrush(QBrush())
        # qp.drawEllipse(QRect(50,100,300,200))
        # # qp.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        # # qp.drawEllipse(e.pos().x(), e.pos().y(), self.brushSize, self.brushSize)
        # self.repaint()

    def drawMask(self):
        self.maskNp=np.zeros((556, 250, 4))
        self.maskNp[:,:,0]=255
        self.maskNp[:,:,3]=128
        self.painter.drawPixmap(self.imgPoint, QPixmap(qimage2ndarray.array2qimage(self.maskNp)))
        print('draw mask')
        pass

    def paintEvent(self, QPaintEvent):
        self.painter.begin(self)
        self.drawImg()
        self.drawMask()
        self.drawGuideLine()
        self.painter.end()