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
from drop.qt.ui.drop.mainUI import  Ui_MainWindow
from qt.com.ImageShower import ImageShower
class mainWindowImp(Ui_MainWindow):
    def setupUi(self, MainWindow,ctPath=r'E:\pyWorkspace\stevenUI\res\ct.tif',suvPath=r'E:\pyWorkspace\stevenUI\res\suv.tif',
                gtPath=r'E:\pyWorkspace\stevenUI\res\gt.bmp',prePath=r'E:\pyWorkspace\stevenUI\res\pre.bmp'):
        super().setupUi(MainWindow)
        self.ctILabel = ImageShower(self.mFrame, imagePath=ctPath)
        self.ctILabel.setGeometry(QtCore.QRect(60, 50, 231, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ctILabel.setFont(font)
        self.ctILabel.setStyleSheet("background-color:#aaaaaa")
        self.ctILabel.setObjectName("ctILabel")

        self.petILabel = ImageShower(self.mFrame, imagePath=suvPath)
        self.petILabel.setGeometry(QtCore.QRect(310, 50, 231, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.petILabel.setFont(font)
        self.petILabel.setStyleSheet("background-color:#aaaaaa")
        self.petILabel.setObjectName("petILabel")

        self.gtSegILabel = ImageShower(self.mFrame, imagePath=gtPath)
        self.gtSegILabel.setGeometry(QtCore.QRect(560, 50, 231, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gtSegILabel.setFont(font)
        self.gtSegILabel.setStyleSheet("background-color:#aaaaaa")
        self.gtSegILabel.setObjectName("gtSegILabel")

from PyQt5 import QtCore,QtGui,QtWidgets
if __name__ == '__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ctPath = r'..\..\res\ct.tif'
    suvPath = r'..\..\res\suv.tif'
    gtPath = r'..\..\res\pre.bmp'
    prePath = r'..\..\res\pre.bmp'
    ui = mainWindowImp()
    ui.setupUi(MainWindow, ctPath=ctPath, suvPath=suvPath, gtPath=gtPath, prePath=prePath)
    MainWindow.show()
    sys.exit(app.exec_())
