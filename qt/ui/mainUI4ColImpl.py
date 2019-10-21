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
from PyQt5 import QtWidgets, QtCore, QtGui

from qt.com.ImageMaskShower import ImageMaskShower
from qt.com.PBDiaImpl import PBDiaImpl
from qt.ui.mainUI4Col import Ui_LymphomaSeg
from qt.com.ImageShower import ImageShower
from qt.com.ImageDrawer import ImageDrawer
from typing import List
from skimage import io as skio
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtWidgets import QApplication
from qt.Utils.LoadDataTh import LoadDataTh
from qt.com.AboutNetDia import Ui_Dialog as ABoutNet
from qt.com.AboutDia import Ui_Dialog as About
from natsort import natsorted
from glob import glob

ILabelW = 230
ILabelH = 450
import numpy as np

patientsData = {'63': {'name': '张文茂', 'gender': '男', 'birthday': '197706', 'checkday': '201702',
                       'doc':'1、腹膜后淋巴结增大，代谢增高；左侧锁骨上窝略增大淋巴结，代谢增高；'
                             '不除外恶性病变（淋巴瘤）可能，建议活检\n'
                             '2、脾脏体积增大，代谢未见异常，请随诊观察'
                            '3、扫描野内骨髓弥漫性代谢增高，考虑反应性改变，请结合临床\n'
                             '4、右肺上叶胸膜下小结节灶，代谢未见明显异常，建议定期随诊复查\n'
                             '5、脂肪肝\n'
                             '6、左侧股骨头致密骨岛；颈、胸、腰椎退行性变\n'
                             '7、双侧基底节区腔隙性脑梗塞；双侧上颌窦炎'}}

dataPath = r'E:\dataset'


# dataPath=r'G:\63'
class mainWindowImp(Ui_LymphomaSeg, QWidget):

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
        self.dataLoaded = False



        def saveResult():
            filename = QFileDialog.getExistingDirectory(self, '选取文件夹', r'E:\test')
            print('filename', filename)
            skio.imsave(os.path.join(filename, '1.png'), self.gtSegILabel.getMask() * 255)

        self.saveResult.triggered.connect(saveResult)

        # def aboutDenseX():
        #     print('about denseX')
        #
        #     aboutNetMain.setWindowModality(Qt.ApplicationModal)
        #     # aboutNetMain.setWindowFlag(Qt.FramelessWindowHint)
        #     aboutNetMain.show()
        #     print('about denseX aaaa')
        #
        # self.aboutDenseXItem.triggered.connect(aboutDenseX)

        def aboutSw():
            print('关于本软件')
        self.aboutItem.triggered.connect(aboutSw)



        def updataImgInShower(index):
            self.ctILabel.setImgNp(self.ctNp[:, :, index])
            self.petILabel.setImgNp(self.suvNp[:, :, index])
            self.gtSegILabel.setImgNp(self.suvNp[:, :, index])
            self.gtSegILabel.setOriMaskNp(self.preNp[:, :, index])
            self.gtSegILabel_2.setImgNp(self.suvNp[:, :, index])
            self.gtSegILabel_2.setMask(self.preNp[:, :, index])

        self.unit = 1

        def openPatient():
            filename = QFileDialog.getExistingDirectory(self, '选取文件夹', dataPath)
            if filename == None or filename == '':
                return

            self.loadDataTh.setFileName(filename)
            self.loadDataTh.start()

            pdiMain = QtWidgets.QMainWindow()
            pdiMain.setFixedHeight(100)
            pd = PBDiaImpl()
            pd.setupUi(pdiMain)
            pdiMain.setWindowModality(Qt.ApplicationModal)
            pdiMain.setWindowFlag(Qt.FramelessWindowHint)
            pdiMain.show()

            i = 0
            waitTime = 1
            while i < 100:

                pd.setValue(i + 1)
                if i < 20:
                    pd.setPanel('读取文件数据……')
                    if i == 19:
                        if self.dataLoaded:
                            i += 1
                        else:
                            i += 0
                    else:
                        i += 1

                    if i == 19 and self.dataLoaded:
                        i += 1



                elif i < 40:
                    waitTime = 2
                    pd.setPanel('解析文件数据……')
                    i += 1
                elif i < 70:
                    waitTime = 2
                    pd.setPanel('加载DenseX-Net与Faster RCNN分割检测模型……')
                    i += 1
                elif i < 90:
                    waitTime = 3
                    pd.setPanel('执行网络辅助分割……')
                    i += 1
                else:
                    waitTime = 1
                    pd.setPanel('图像生成中……')
                    i += 1
                QThread.msleep(int(waitTime * 100))
                QApplication.processEvents()
            i = 0
            waitTime = 0

            self.dataLoaded = False

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


            self.ctLowSpi.setValue(np.min(self.ctNp))
            self.ctHighSpi.setValue(np.max(self.ctNp))
            self.ctLowSpi.setMinimum(np.min(self.ctNp))
            self.ctLowSpi.setMaximum(np.max(self.ctNp))
            self.ctHighSpi.setMinimum(np.min(self.ctNp))
            self.ctHighSpi.setMaximum(np.max(self.ctNp))

            self.ctLowSdr.setMinimum(np.min(self.ctNp))
            self.ctLowSdr.setMaximum(np.max(self.ctNp))
            self.ctHighSdr.setMinimum(np.min(self.ctNp))
            self.ctHighSdr.setMaximum(np.max(self.ctNp))


            self.petLowSpi.setValue(np.min(self.suvNp))
            self.petHighSpi.setValue(np.max(self.suvNp))
            self.petLowSpi.setMinimum(np.min(self.suvNp))
            self.petLowSpi.setMaximum(np.max(self.suvNp))
            self.petHighSpi.setMinimum(np.min(self.suvNp))
            self.petHighSpi.setMaximum(np.max(self.suvNp))

            self.petLowSlider.setMinimum(np.min(self.suvNp))
            self.petLowSlider.setMaximum(np.max(self.suvNp))
            self.petHighSdr.setMinimum(np.min(self.suvNp))
            self.petHighSdr.setMaximum(np.max(self.suvNp))

            print('ct max',np.max(self.ctNp))



            updataImgInShower(self.ctNp.shape[2] // 2)

            def setPanelText(panel, text):
                panel.setText(QtCore.QCoreApplication.translate("Dialog",
                                                                "<html><head/><body><p align=\"center\">" + text + "</p></body></html>"))

            pa = patientsData[os.path.basename(filename)]
            setPanelText(self.nameLab, pa['name'])
            setPanelText(self.genderLab, pa['gender'])
            setPanelText(self.birthLab, pa['birthday'])
            setPanelText(self.checkDataLab, pa['checkday'])
            setPanelText(self.docText,pa['doc'])

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
            print('slider index', sliderIndex)
            # if self.sliceIndexSlider.sliderReleased():

            self.sliceIndexSpi.setValue(sliderIndex)
        self.sliceIndexSlider.valueChanged.connect(sliceIndexSliderListener)
        # self.sliceIndexSlider.sliderReleased.connect(sliceIndexSliderListener)

        def sliceIndexSpiListener():
            print('slice spi value change')
            self.sliceIndexSlider.setValue(self.sliceIndexSpi.value())
            updataImgInShower(self.sliceIndexSpi.value())

        self.sliceIndexSpi.valueChanged.connect(sliceIndexSpiListener)

        def ctHighSdrListener():
            self.ctHighSpi.setValue(int(self.ctHighSdr.value()))
        self.ctHighSdr.valueChanged.connect(ctHighSdrListener)

        def ctLowSdrListener():
            self.ctLowSpi.setValue(int(self.ctLowSdr.value()))

        self.ctLowSdr.valueChanged.connect(ctLowSdrListener)

        def ctHighSpiListener():
            ctHighV=self.ctHighSpi.value()
            ctLowV=self.ctLowSpi.value()
            ctLowV=min(ctLowV,ctHighV)
            self.ctHighSdr.setValue(ctHighV)
            self.ctLowSdr.setValue(ctLowV)
            self.ctLowSpi.setValue(ctLowV)
            self.ctILabel.clipImg(ctLowV,ctHighV)
        self.ctHighSpi.valueChanged.connect(ctHighSpiListener)

        def ctLowSpiListener():
            ctHighV=self.ctHighSpi.value()
            ctLowV=self.ctLowSpi.value()
            ctHighV=max(ctLowV,ctHighV)
            self.ctHighSdr.setValue(ctHighV)
            self.ctLowSdr.setValue(ctLowV)
            self.ctHighSpi.setValue(ctHighV)
            self.ctILabel.clipImg(ctLowV,ctHighV)
        self.ctLowSpi.valueChanged.connect(ctLowSpiListener)




        def petHighSdrListener():
            self.petHighSpi.setValue(int(self.petHighSdr.value()))
        self.petHighSdr.valueChanged.connect(petHighSdrListener)

        def petLowSliderListener():
            self.petLowSpi.setValue(int(self.petLowSlider.value()))
        self.petLowSlider.valueChanged.connect(petLowSliderListener)

        def petHighSpiListener():
            petHighV=self.petHighSpi.value()
            petLowV=self.petLowSpi.value()
            petLowV=min(petLowV,petHighV)
            self.petHighSdr.setValue(petHighV)
            self.petLowSlider.setValue(petLowV)
            self.petLowSpi.setValue(petLowV)
            self.petILabel.clipImg(petLowV,petHighV)
            self.gtSegILabel.clipImg(petLowV, petHighV)
            self.gtSegILabel_2.clipImg(petLowV, petHighV)
        self.petHighSpi.valueChanged.connect(petHighSpiListener)

        def petLowSpiListener():
            petHighV=self.petHighSpi.value()
            petLowV=self.petLowSpi.value()
            petHighV=max(petLowV,petHighV)
            self.petHighSdr.setValue(petHighV)
            self.petLowSlider.setValue(petLowV)
            self.petHighSpi.setValue(petHighV)
            self.petILabel.clipImg(petLowV,petHighV)
            self.gtSegILabel.clipImg(petLowV,petHighV)
            self.gtSegILabel_2.clipImg(petLowV,petHighV)
        self.petLowSpi.valueChanged.connect(petLowSpiListener)

    def loadData(self, data):
        # ctData,suvData,preData):
        print('loadData run')
        self.ctNp = data[0]
        self.suvNp = data[1]
        self.preNp = data[2]
        self.dataLoaded = True


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

    aboutNetMain = QtWidgets.QDialog()
    aboutNetMain.setFixedHeight(600)
    an = ABoutNet()
    an.setupUi(aboutNetMain)
    def aboutDenseX():
        print('about denseX')
        aboutNetMain.setWindowModality(Qt.ApplicationModal)
        aboutNetMain.setFixedHeight(400)
        # aboutNetMain.setWindowFlag(Qt.FramelessWindowHint)
        aboutNetMain.show()
        print('about denseX aaaa')
    print('set ui')
    ui.aboutDenseXItem.triggered.connect(aboutDenseX)

    aboutMain = QtWidgets.QDialog()
    aboutMain.setFixedHeight(600)
    a = About()
    a.setupUi(aboutMain)


    def about():
        print('about denseX')
        aboutMain.setWindowModality(Qt.ApplicationModal)
        aboutMain.setFixedHeight(150)
        # aboutNetMain.setWindowFlag(Qt.FramelessWindowHint)
        aboutMain.show()
        print('about denseX aaaa')

    ui.aboutItem.triggered.connect(about)

    MainWindow.show()
    sys.exit(app.exec_())

