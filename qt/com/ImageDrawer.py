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
from .ImageShower import  ImageShower
class ImageDrawer(ImageShower):
    def __init__(self,parent=None, imagePath=r'E:\pyWorkspace\stevenUI\res\ct.tif'):
        super().__init__(parent)
        print(' init imageDrawer')
        self.brushDraw=True
        self.brushSize=3

    def updateDrawerSize(self,size):
        self.brushSize=size
        print('drawer size',size)


    def updateDrawerMode(self,draw):
        if draw==1:
            print('切换为添加模式')
        elif draw==-1:
            print('切换为删除模式')
        else:
            print('切换为关闭模式')
        self.brushDraw=draw
