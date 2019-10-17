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
 @Author = 'steven'   @DateTime = '2019/10/17 15:06'
'''
from .ImageShower import ImageShower, QSize
from skimage import  io as skio
import numpy as np
class ImageMaskShower(ImageShower):
    def __init__(self,parent,imagePath,maskPath):
        super().__init__(parent,imagePath)



        self.alpha=128
        self.maskNp=(skio.imread(maskPath)>0).astype(np.uint8)
        self.oriMaskNp = (skio.imread(maskPath) > 0).astype(np.uint8)

    def setMask(self, mask=None):
        if not mask:
            mask = np.zeros((self.maskNp.shape[0], self.maskNp.shape[1]))
        self.maskNp = int(mask > 0)
        self.repaint()

    def recoverAutoSeg(self):
        self.maskNp=self.oriMaskNp
        self.repaint()

    def paintEvent(self, QPaintEvent):
        self.painter.begin(self)
        self.drawImg()
        self.drawMask()
        self.drawGuideLine()
        self.painter.end()

    def drawMask(self):
        zNp = np.zeros((self.maskNp.shape[0], self.maskNp.shape[1]))
        showMask = np.stack([self.maskNp * 255, zNp, zNp, self.maskNp * self.alpha], axis=2)
        self.painter.drawPixmap(self.imgPoint, self.np2QPixmap(showMask).scaled(QSize(*self.showImgScale)))

    def updateLocValueWatcher(self, mouseImgPoint):
        if self.hasLocWatcher:
            self.v.setText(str(int(self.maskNp[mouseImgPoint.y(), mouseImgPoint.x()])))
    def setMask(self,mask=None):
        # if mask == None:
        #     mask=np.zeros((self.maskNp.shape[0],self.maskNp.shape[1]))
        self.maskNp = (mask>0).astype(np.uint8)
        self.repaint()
    def getMask(self):
        return self.maskNp