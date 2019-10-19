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
from PyQt5 import QtWidgets,QtCore,QtGui

from qt.com.ImageMaskShower import ImageMaskShower
from qt.com.PBDiaImpl import PBDiaImpl
from qt.ui.mainUI4Col import Ui_MainWindow
from qt.com.ImageShower import ImageShower
from qt.com.ImageDrawer import ImageDrawer
from typing import List
from skimage import io as skio
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtCore import QThread,Qt
from PyQt5.QtWidgets import QApplication
from qt.Utils.LoadDataTh import  LoadDataTh



from natsort import natsorted
from glob import glob

ILabelW = 230
ILabelH = 450
import numpy as np
patientsData={'63':{'name':'张文茂','gender':'男','birthday':'197706','checkday':'201702'}}

# dataPath=r'E:\dataset'
dataPath=r'G:\63'
class mainWindowImp(Ui_MainWindow, QWidget):

    def setupUi(self, MainWindow, ctPath=r'E:\pyWorkspace\stevenUI\res\ct.tif',
                suvPath=r'E:\pyWorkspace\stevenUI\res\suv.tif',
                gtPath=r'E:\pyWorkspace\stevenUI\res\gt.bmp',
                prePath=r'E:\pyWorkspace\stevenUI\res\pre.bmp'):
        super().setupUi(MainWindow)
        self.ctNp = np.zeros((250, 250, 530))
        self.suvNp = np.zeros((250, 250, 530))
        self.preNp = np.zeros((250, 250, 530))
        self.ctILabel = ImageShower(self.mFrame, image=np.zeros((250, 530)))
        self.ctILabel.setGeometry(QtCore.QRect(60, 50, ILabelW, ILabelH))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ctILabel.setFont(font)
        self.ctILabel.setStyleSheet("background-color:#aaaaaa")
        self.ctILabel.setObjectName("ctILabel")
        self.ctILabel.setLocWatcher(self.xLab, self.yLab, self.ctLab)

        self.petILabel = ImageShower(self.mFrame, image=np.zeros((250, 530)))
        self.petILabel.setGeometry(QtCore.QRect(310, 50, 230, ILabelH))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.petILabel.setFont(font)
        self.petILabel.setStyleSheet("background-color:#aaaaaa")
        self.petILabel.setObjectName("petILabel")
        self.petILabel.setLocWatcher(self.xLab, self.yLab, self.petLab)

        self.gtSegILabel = ImageMaskShower(self.mFrame, image=np.zeros((250, 530)), mask=np.zeros((250, 530)))
        self.gtSegILabel.setGeometry(QtCore.QRect(560, 50, ILabelW, ILabelH))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gtSegILabel.setFont(font)
        self.gtSegILabel.setStyleSheet("background-color:#aaaaaa")
        self.gtSegILabel.setObjectName("gtSegILabel")
        self.gtSegILabel.setLocWatcher(self.xLab, self.yLab, self.maskLab)

        self.gtSegILabel_2 = ImageDrawer(self.mFrame, image=np.zeros((250, 530)), mask=np.zeros((250, 530)))
        self.gtSegILabel_2.setGeometry(QtCore.QRect(810, 50, ILabelW, ILabelH))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gtSegILabel_2.setFont(font)
        self.gtSegILabel_2.setStyleSheet("background-color:#0000aa")
        self.gtSegILabel_2.setObjectName("gtSegILabel_2")

        self.loadDataTh = LoadDataTh()
        self.loadDataTh.loadDataSignal.connect(self.loadData)
        self.dataLoaded=False

        def saveResult():
            filename = QFileDialog.getExistingDirectory(self, '选取文件夹', r'E:\test')
            print('filename', filename)
            skio.imsave(os.path.join(filename, '1.png'), self.gtSegILabel.getMask() * 255)

        self.saveResult.triggered.connect(saveResult)

        def updataImgInShower(index):
            self.ctILabel.setImgNp(self.ctNp[:, :, index])
            self.petILabel.setImgNp(self.suvNp[:, :, index])
            self.gtSegILabel.setImgNp(self.suvNp[:, :, index])
            self.gtSegILabel.setOriMaskNp(self.preNp[:, :, index])
            self.gtSegILabel_2.setImgNp(self.suvNp[:, :, index])
            self.gtSegILabel_2.setMask(self.preNp[:, :, index])

        self.unit=1

        def openPatient():
            filename = QFileDialog.getExistingDirectory(self, '选取文件夹', dataPath)
            if filename==None or filename=='':
                return

            self.loadDataTh.setFileName(filename)
            self.loadDataTh.start()

            pdiMain=QtWidgets.QMainWindow()
            pdiMain.setFixedHeight(100)
            pd=PBDiaImpl()
            pd.setupUi(pdiMain)
            pdiMain.setWindowModality(Qt.ApplicationModal)
            pdiMain.setWindowFlag(Qt.FramelessWindowHint)
            pdiMain.show()




            i=0
            waitTime=1
            while i<100:

                pd.setValue(i + 1)
                if i<20:
                    pd.setPanel('读取文件数据……')
                    if i==19 :
                        if self.dataLoaded:
                            i+=1
                        else:
                            i+=0
                    else:
                        i+=1

                    if i==19 and  self.dataLoaded:
                        i+=1



                elif i<40:
                    waitTime=2
                    pd.setPanel('解析文件数据……')
                    i += 1
                elif i<90:
                    waitTime=3
                    pd.setPanel('进行辅助分割……')
                    i += 1
                else:
                    waitTime=1
                    pd.setPanel('图像生成中……')
                    i += 1
                QThread.msleep(int(waitTime * 100))
                QApplication.processEvents()
            i=0
            waitTime=0

            self.dataLoaded=False




            # ctps = natsorted(glob(os.path.join(filename, '[0-9]*ct.tif')))
            # suvps = natsorted(glob(os.path.join(filename, '[0-9]*suv.tif')))
            # pres = natsorted(glob(os.path.join(filename, '[0-9]*preMd.bmp')))
            # self.ctNp = np.array([skio.imread(i) for i in ctps]).transpose((0, 2, 1))
            #
            # self.suvNp = np.array([skio.imread(i) for i in suvps]).transpose((0, 2, 1))
            # self.preNp = np.array([skio.imread(i) for i in pres]).transpose((0, 2, 1))

            self.sliceIndexSlider.setMaximum(self.ctNp.shape[2])
            self.sliceIndexSlider.setValue(self.ctNp.shape[2] // 2)
            self.sliceIndexSpi.setMaximum(self.ctNp.shape[2])
            self.sliceIndexSpi.setValue(self.ctNp.shape[2] // 2)
            updataImgInShower(self.ctNp.shape[2] // 2)

            def setPanelText(panel,text):
                panel.setText(QtCore.QCoreApplication.translate ("Dialog", "<html><head/><body><p align=\"center\">"+text+"</p></body></html>"))
            pa=patientsData[os.path.basename(filename)]
            setPanelText( self.nameLab,pa['name'])
            setPanelText(self.genderLab,pa['gender'])
            setPanelText(self.birthLab,pa['birthday'])
            setPanelText(self.checkDataLab,pa['checkday'])

        self.openMenuItem.triggered.connect(openPatient)

        def makeFriendShower(friends: List[ImageShower]):
            '''
            将几个ImageShower互相添加友视图
            :param friends:
            :return:
            '''
            for shower in friends:
                shower.setFriendWatcher([i for i in friends if i != shower])

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



        self.sliceIndexSlider.setValue(self.ctNp.shape[2] // 2)
        self.sliceIndexSlider.setMinimum(0)
        self.sliceIndexSlider.setMaximum(1)
        def sliceIndexSliderListener():
            sliderIndex = int(self.sliceIndexSlider.value())
            print('slider index',sliderIndex)
            # if self.sliceIndexSlider.sliderReleased():

            self.sliceIndexSpi.setValue(sliderIndex)

        self.sliceIndexSlider.sliderReleased.connect(sliceIndexSliderListener)

        def sliceIndexSpiListener():
            print('slice spi value change')
            self.sliceIndexSlider.setValue(self.sliceIndexSpi.value())
            updataImgInShower(self.sliceIndexSpi.value())
        self.sliceIndexSpi.valueChanged.connect(sliceIndexSpiListener)
        # def sliceIndexEtListener():
        #     print(' slice et trigged')
        # self.sliceIndexEt.returnPressed.connect(sliceIndexEtListener)
        # def sliceIndex

    def loadData(self,data):
        # ctData,suvData,preData):
        print('loadData run')
        self.ctNp=data[0]
        self.suvNp=data[1]
        self.preNp=data[2]
        self.dataLoaded=True


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
