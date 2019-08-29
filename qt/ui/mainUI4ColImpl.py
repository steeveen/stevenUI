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
 @Author = 'steven'   @DateTime = '2019/8/21 14:30'
'''
from qt.ui.mainUI4Col import  Ui_MainWindow
from qt.com.ImageShower import ImageShower
class mainWindowImp(Ui_MainWindow):
    def setupUi(self, MainWindow,ctPath=r'E:\pyWorkspace\stevenUI\res\ct.tif',suvPath=r'E:\pyWorkspace\stevenUI\res\suv.tif',
                gtPath=r'E:\pyWorkspace\stevenUI\res\gt.bmp',prePath=r'E:\pyWorkspace\stevenUI\res\pre.bmp'):
        super().setupUi(MainWindow)
        self.ctILabel = ImageShower(self.mFrame, imagePath=ctPath)
        self.ctILabel.setGeometry(QtCore.QRect(60, 50, 230, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ctILabel.setFont(font)
        self.ctILabel.setStyleSheet("background-color:#aaaaaa")
        self.ctILabel.setObjectName("ctILabel")
        self.ctILabel.setLocWatcher(self.xLab,self.yLab,self.ctLab)

        self.petILabel = ImageShower(self.mFrame, imagePath=suvPath)
        self.petILabel.setGeometry(QtCore.QRect(310, 50, 230, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.petILabel.setFont(font)
        self.petILabel.setStyleSheet("background-color:#aaaaaa")
        self.petILabel.setObjectName("petILabel")
        self.petILabel.setLocWatcher(self.xLab, self.yLab, self.petLab)

        self.gtSegILabel = ImageShower(self.mFrame, imagePath=prePath)
        self.gtSegILabel.setGeometry(QtCore.QRect(560, 50, 230, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gtSegILabel.setFont(font)
        self.gtSegILabel.setStyleSheet("background-color:#aaaaaa")
        self.gtSegILabel.setObjectName("gtSegILabel")

        self.gtSegILabel_2 = ImageShower(self.mFrame, imagePath=gtPath)
        self.gtSegILabel_2.setGeometry(QtCore.QRect(810, 50, 230, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gtSegILabel_2.setFont(font)
        self.gtSegILabel_2.setStyleSheet("background-color:#0000aa")
        self.gtSegILabel_2.setObjectName("gtSegILabel_2")

from PyQt5 import QtCore,QtGui,QtWidgets
if __name__ == '__main__':
    import sys
    import os
    app=QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ctPath = r'..\..\res\ct.tif'
    suvPath = r'..\..\res\suv.tif'
    gtPath = r'..\..\res\gt.bmp'
    prePath = r'..\..\res\pre.bmp'
    ui = mainWindowImp()
    ui.setupUi(MainWindow, ctPath=ctPath, suvPath=suvPath, gtPath=gtPath, prePath=prePath)
    ui.statusbar.showMessage('Huiyan Jiang Lab, Software College, Northeastern University(NEU), Shenyang, Liaoning, China')
    MainWindow.show()
    sys.exit(app.exec_())
