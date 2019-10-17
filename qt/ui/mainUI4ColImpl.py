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
from qt.com.ImageMaskShower import ImageMaskShower
from qt.ui.mainUI4Col import Ui_MainWindow
from qt.com.ImageShower import ImageShower
from qt.com.ImageDrawer import ImageDrawer
from typing import List
from skimage import io as skio
from PyQt5.QtWidgets import QFileDialog, QWidget

ILabelW = 230
ILabelH = 450


class mainWindowImp(Ui_MainWindow, QWidget):

    def setupUi(self, MainWindow, ctPath=r'E:\pyWorkspace\stevenUI\res\ct.tif',
                suvPath=r'E:\pyWorkspace\stevenUI\res\suv.tif',
                gtPath=r'E:\pyWorkspace\stevenUI\res\gt.bmp', prePath=r'E:\pyWorkspace\stevenUI\res\pre.bmp'):
        super().setupUi(MainWindow)
        self.ctILabel = ImageShower(self.mFrame, imagePath=ctPath)
        self.ctILabel.setGeometry(QtCore.QRect(60, 50, ILabelW, ILabelH))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ctILabel.setFont(font)
        self.ctILabel.setStyleSheet("background-color:#aaaaaa")
        self.ctILabel.setObjectName("ctILabel")
        self.ctILabel.setLocWatcher(self.xLab, self.yLab, self.ctLab)

        self.petILabel = ImageShower(self.mFrame, imagePath=suvPath)
        self.petILabel.setGeometry(QtCore.QRect(310, 50, 230, ILabelH))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.petILabel.setFont(font)
        self.petILabel.setStyleSheet("background-color:#aaaaaa")
        self.petILabel.setObjectName("petILabel")
        self.petILabel.setLocWatcher(self.xLab, self.yLab, self.petLab)

        self.gtSegILabel = ImageMaskShower(self.mFrame,imagePath=suvPath, maskPath=prePath)
        self.gtSegILabel.setGeometry(QtCore.QRect(560, 50, ILabelW, ILabelH))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gtSegILabel.setFont(font)
        self.gtSegILabel.setStyleSheet("background-color:#aaaaaa")
        self.gtSegILabel.setObjectName("gtSegILabel")
        self.gtSegILabel.setLocWatcher(self.xLab, self.yLab, self.maskLab)

        self.gtSegILabel_2 = ImageDrawer(self.mFrame, imagePath=suvPath, maskPath=prePath)
        self.gtSegILabel_2.setGeometry(QtCore.QRect(810, 50, ILabelW, ILabelH))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gtSegILabel_2.setFont(font)
        self.gtSegILabel_2.setStyleSheet("background-color:#0000aa")
        self.gtSegILabel_2.setObjectName("gtSegILabel_2")

        def saveResult():
            filename = QFileDialog.getExistingDirectory(self, '选取文件夹', r'E:\test')
            print('filename', filename)
            skio.imsave(os.path.join(filename, '1.png'), self.gtSegILabel.getMask()*255)


        def makeFriendShower(friends: List[ImageShower]):
            '''
            将几个ImageShower互相添加友视图
            :param friends:
            :return:
            '''
            for shower in friends:
                shower.setFriendWatcher([i for i in friends if i != shower])

        self.saveResult.triggered.connect(saveResult)
        makeFriendShower([self.ctILabel, self.petILabel, self.gtSegILabel, self.gtSegILabel_2])


        def addSegListener():
            if self.addSegBtn.isChecked():
                self.delSegBtn.setChecked(False)
                self.gtSegILabel_2.updateDrawerMode(1)
            else:
                self.gtSegILabel_2.updateDrawerMode(0)
        def delSegListener():
            if self.delSegBtn.isChecked():
                self.addSegBtn.setChecked(False)
                self.gtSegILabel_2.updateDrawerMode(-1)
            else:
                self.gtSegILabel_2.updateDrawerMode(0)
        self.addSegBtn.clicked.connect(addSegListener)
        self.delSegBtn.clicked.connect(delSegListener)

        self.brushSizeSpi.setValue(self.gtSegILabel_2.brushSize)
        def spinChangeListener():
            self.gtSegILabel_2.updateDrawerSize(self.brushSizeSpi.value())
        self.brushSizeSpi.valueChanged.connect(spinChangeListener)

        def resetSeg2():
            self.gtSegILabel_2.setMask(self.gtSegILabel.getMask())
        self.resetSegBtn.clicked.connect(resetSeg2)

        def confSeg2():
            self.gtSegILabel.setMask(self.gtSegILabel_2.getMask())
        self.confSegBtn.clicked.connect(confSeg2)

        def recoverSeg():
            self.gtSegILabel.recoverAutoSeg()
        self.recoverSegBtn.clicked.connect(recoverSeg)




from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    import sys
    import os

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ctPath = r'..\..\res\ct.tif'
    suvPath = r'..\..\res\suv.tif'
    gtPath = r'..\..\res\gt.bmp'
    prePath = r'..\..\res\pre.bmp'
    ui = mainWindowImp()
    ui.setupUi(MainWindow, ctPath=ctPath, suvPath=suvPath, gtPath=gtPath, prePath=prePath)
    ui.statusbar.showMessage(
        'Huiyan Jiang Lab, Software College, Northeastern University(NEU), Shenyang, Liaoning, China')
    MainWindow.show()
    sys.exit(app.exec_())
