# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI4Col.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1134, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mFrame = QtWidgets.QFrame(self.centralwidget)
        self.mFrame.setGeometry(QtCore.QRect(0, 0, 1131, 721))
        self.mFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mFrame.setObjectName("mFrame")
        self.ctLabel = QtWidgets.QLabel(self.mFrame)
        self.ctLabel.setGeometry(QtCore.QRect(60, 10, 231, 31))
        self.ctLabel.setStyleSheet("background-color:#bbbbbb")
        self.ctLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ctLabel.setObjectName("ctLabel")
        self.petLabel = QtWidgets.QLabel(self.mFrame)
        self.petLabel.setGeometry(QtCore.QRect(310, 10, 231, 31))
        self.petLabel.setStyleSheet("background-color:#bbbbbb")
        self.petLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.petLabel.setObjectName("petLabel")
        self.gtSegLabel = QtWidgets.QLabel(self.mFrame)
        self.gtSegLabel.setGeometry(QtCore.QRect(560, 10, 231, 31))
        self.gtSegLabel.setStyleSheet("background-color:#bbbbbb")
        self.gtSegLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gtSegLabel.setObjectName("gtSegLabel")
        self.ctILabel = QtWidgets.QLabel(self.mFrame)
        self.ctILabel.setGeometry(QtCore.QRect(60, 50, 231, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ctILabel.setFont(font)
        self.ctILabel.setStyleSheet("background-color:#aaaaaa")
        self.ctILabel.setText("")
        self.ctILabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ctILabel.setObjectName("ctILabel")
        self.petILabel = QtWidgets.QLabel(self.mFrame)
        self.petILabel.setGeometry(QtCore.QRect(310, 50, 231, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.petILabel.setFont(font)
        self.petILabel.setStyleSheet("background-color:#aaaaaa")
        self.petILabel.setText("")
        self.petILabel.setAlignment(QtCore.Qt.AlignCenter)
        self.petILabel.setObjectName("petILabel")
        self.gtSegILabel = QtWidgets.QLabel(self.mFrame)
        self.gtSegILabel.setGeometry(QtCore.QRect(560, 50, 231, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gtSegILabel.setFont(font)
        self.gtSegILabel.setStyleSheet("background-color:#aaaaaa")
        self.gtSegILabel.setText("")
        self.gtSegILabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gtSegILabel.setObjectName("gtSegILabel")
        self.groupBox = QtWidgets.QGroupBox(self.mFrame)
        self.groupBox.setGeometry(QtCore.QRect(10, 650, 571, 51))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 20, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(290, 20, 54, 16))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(440, 20, 54, 16))
        self.label_9.setObjectName("label_9")
        self.genderLab = QtWidgets.QLabel(self.groupBox)
        self.genderLab.setGeometry(QtCore.QRect(190, 20, 54, 16))
        self.genderLab.setStyleSheet("background-color:#aaaaaa")
        self.genderLab.setAlignment(QtCore.Qt.AlignCenter)
        self.genderLab.setObjectName("genderLab")
        self.checkDataLab = QtWidgets.QLabel(self.groupBox)
        self.checkDataLab.setGeometry(QtCore.QRect(500, 20, 54, 16))
        self.checkDataLab.setStyleSheet("background-color:#aaaaaa")
        self.checkDataLab.setLineWidth(8)
        self.checkDataLab.setAlignment(QtCore.Qt.AlignCenter)
        self.checkDataLab.setObjectName("checkDataLab")
        self.birthLab = QtWidgets.QLabel(self.groupBox)
        self.birthLab.setGeometry(QtCore.QRect(350, 20, 54, 16))
        self.birthLab.setStyleSheet("background-color:#aaaaaa")
        self.birthLab.setAlignment(QtCore.Qt.AlignCenter)
        self.birthLab.setObjectName("birthLab")
        self.nameLab = QtWidgets.QLabel(self.groupBox)
        self.nameLab.setGeometry(QtCore.QRect(60, 20, 54, 16))
        self.nameLab.setStyleSheet("background-color:#aaaaaa")
        self.nameLab.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLab.setObjectName("nameLab")
        self.groupBox_3 = QtWidgets.QGroupBox(self.mFrame)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 580, 571, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(32, 22, 23, 16))
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_3)
        self.label_27.setGeometry(QtCore.QRect(120, 22, 23, 16))
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.yLab = QtWidgets.QLabel(self.groupBox_3)
        self.yLab.setGeometry(QtCore.QRect(140, 22, 31, 16))
        self.yLab.setStyleSheet("background-color:#aaaaaa")
        self.yLab.setAlignment(QtCore.Qt.AlignCenter)
        self.yLab.setObjectName("yLab")
        self.xLab = QtWidgets.QLabel(self.groupBox_3)
        self.xLab.setGeometry(QtCore.QRect(50, 22, 31, 16))
        self.xLab.setStyleSheet("background-color:#aaaaaa")
        self.xLab.setAlignment(QtCore.Qt.AlignCenter)
        self.xLab.setObjectName("xLab")
        self.zLab = QtWidgets.QLabel(self.groupBox_3)
        self.zLab.setGeometry(QtCore.QRect(230, 22, 31, 16))
        self.zLab.setStyleSheet("background-color:#aaaaaa")
        self.zLab.setAlignment(QtCore.Qt.AlignCenter)
        self.zLab.setObjectName("zLab")
        self.label_35 = QtWidgets.QLabel(self.groupBox_3)
        self.label_35.setGeometry(QtCore.QRect(209, 22, 23, 16))
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.maskLab = QtWidgets.QLabel(self.groupBox_3)
        self.maskLab.setGeometry(QtCore.QRect(530, 22, 31, 16))
        self.maskLab.setStyleSheet("background-color:#aaaaaa")
        self.maskLab.setAlignment(QtCore.Qt.AlignCenter)
        self.maskLab.setObjectName("maskLab")
        self.label_28 = QtWidgets.QLabel(self.groupBox_3)
        self.label_28.setGeometry(QtCore.QRect(391, 22, 26, 16))
        self.label_28.setObjectName("label_28")
        self.petLab = QtWidgets.QLabel(self.groupBox_3)
        self.petLab.setGeometry(QtCore.QRect(420, 22, 31, 16))
        self.petLab.setStyleSheet("background-color:#aaaaaa")
        self.petLab.setAlignment(QtCore.Qt.AlignCenter)
        self.petLab.setObjectName("petLab")
        self.label_37 = QtWidgets.QLabel(self.groupBox_3)
        self.label_37.setGeometry(QtCore.QRect(490, 22, 31, 16))
        self.label_37.setObjectName("label_37")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(300, 22, 25, 16))
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.ctLab = QtWidgets.QLabel(self.groupBox_3)
        self.ctLab.setGeometry(QtCore.QRect(320, 22, 31, 16))
        self.ctLab.setStyleSheet("background-color:#aaaaaa")
        self.ctLab.setAlignment(QtCore.Qt.AlignCenter)
        self.ctLab.setObjectName("ctLab")
        self.sliceIndexSlider = QtWidgets.QSlider(self.mFrame)
        self.sliceIndexSlider.setGeometry(QtCore.QRect(20, 52, 22, 421))
        self.sliceIndexSlider.setProperty("value", 99)
        self.sliceIndexSlider.setOrientation(QtCore.Qt.Vertical)
        self.sliceIndexSlider.setObjectName("sliceIndexSlider")
        self.sliceIndexEt = QtWidgets.QLineEdit(self.mFrame)
        self.sliceIndexEt.setGeometry(QtCore.QRect(10, 480, 41, 20))
        self.sliceIndexEt.setObjectName("sliceIndexEt")
        self.line = QtWidgets.QFrame(self.mFrame)
        self.line.setGeometry(QtCore.QRect(10, 560, 1071, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_5 = QtWidgets.QGroupBox(self.mFrame)
        self.groupBox_5.setGeometry(QtCore.QRect(620, 580, 421, 131))
        self.groupBox_5.setStyleSheet("background-color:rgb(170, 170, 255)")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_8 = QtWidgets.QLabel(self.mFrame)
        self.label_8.setGeometry(QtCore.QRect(20, 515, 28, 12))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_19 = QtWidgets.QLabel(self.mFrame)
        self.label_19.setGeometry(QtCore.QRect(20, 545, 28, 12))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.ctLowSdr = QtWidgets.QSlider(self.mFrame)
        self.ctLowSdr.setGeometry(QtCore.QRect(60, 510, 181, 22))
        self.ctLowSdr.setOrientation(QtCore.Qt.Horizontal)
        self.ctLowSdr.setObjectName("ctLowSdr")
        self.ctHighSdr = QtWidgets.QSlider(self.mFrame)
        self.ctHighSdr.setGeometry(QtCore.QRect(60, 540, 181, 22))
        self.ctHighSdr.setProperty("value", 99)
        self.ctHighSdr.setOrientation(QtCore.Qt.Horizontal)
        self.ctHighSdr.setObjectName("ctHighSdr")
        self.ctlowEt = QtWidgets.QLineEdit(self.mFrame)
        self.ctlowEt.setGeometry(QtCore.QRect(250, 510, 41, 20))
        self.ctlowEt.setObjectName("ctlowEt")
        self.ctHighEt = QtWidgets.QLineEdit(self.mFrame)
        self.ctHighEt.setGeometry(QtCore.QRect(250, 540, 41, 20))
        self.ctHighEt.setObjectName("ctHighEt")
        self.petLowEt = QtWidgets.QLineEdit(self.mFrame)
        self.petLowEt.setGeometry(QtCore.QRect(500, 510, 41, 20))
        self.petLowEt.setObjectName("petLowEt")
        self.petHighEt = QtWidgets.QLineEdit(self.mFrame)
        self.petHighEt.setGeometry(QtCore.QRect(500, 540, 41, 20))
        self.petHighEt.setObjectName("petHighEt")
        self.petHighSdr = QtWidgets.QSlider(self.mFrame)
        self.petHighSdr.setGeometry(QtCore.QRect(310, 540, 181, 22))
        self.petHighSdr.setProperty("value", 99)
        self.petHighSdr.setOrientation(QtCore.Qt.Horizontal)
        self.petHighSdr.setObjectName("petHighSdr")
        self.petLowSlider = QtWidgets.QSlider(self.mFrame)
        self.petLowSlider.setGeometry(QtCore.QRect(310, 510, 181, 22))
        self.petLowSlider.setOrientation(QtCore.Qt.Horizontal)
        self.petLowSlider.setObjectName("petLowSlider")
        self.label_4 = QtWidgets.QLabel(self.mFrame)
        self.label_4.setGeometry(QtCore.QRect(15, 10, 31, 31))
        self.label_4.setObjectName("label_4")
        self.gtSegLabel_2 = QtWidgets.QLabel(self.mFrame)
        self.gtSegLabel_2.setGeometry(QtCore.QRect(810, 10, 231, 31))
        self.gtSegLabel_2.setStyleSheet("background-color:#bbbbbb")
        self.gtSegLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gtSegLabel_2.setObjectName("gtSegLabel_2")
        self.gtSegILabel_2 = QtWidgets.QLabel(self.mFrame)
        self.gtSegILabel_2.setGeometry(QtCore.QRect(810, 50, 231, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gtSegILabel_2.setFont(font)
        self.gtSegILabel_2.setStyleSheet("background-color:#aaaaaa")
        self.gtSegILabel_2.setText("")
        self.gtSegILabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gtSegILabel_2.setObjectName("gtSegILabel_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1134, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ctLabel.setText(_translate("MainWindow", "CT"))
        self.petLabel.setText(_translate("MainWindow", "PET"))
        self.gtSegLabel.setText(_translate("MainWindow", "Segmentation"))
        self.groupBox.setTitle(_translate("MainWindow", "患者信息"))
        self.label.setText(_translate("MainWindow", "姓名："))
        self.label_2.setText(_translate("MainWindow", "性别："))
        self.label_3.setText(_translate("MainWindow", "出生年月："))
        self.label_9.setText(_translate("MainWindow", "检查日期："))
        self.genderLab.setText(_translate("MainWindow", "男"))
        self.checkDataLab.setText(_translate("MainWindow", "201701"))
        self.birthLab.setText(_translate("MainWindow", "197706"))
        self.nameLab.setText(_translate("MainWindow", "XXX"))
        self.groupBox_3.setTitle(_translate("MainWindow", "坐标信息"))
        self.label_26.setText(_translate("MainWindow", "X："))
        self.label_27.setText(_translate("MainWindow", "Y："))
        self.yLab.setText(_translate("MainWindow", "40"))
        self.xLab.setText(_translate("MainWindow", "20"))
        self.zLab.setText(_translate("MainWindow", "30"))
        self.label_35.setText(_translate("MainWindow", "Z："))
        self.maskLab.setText(_translate("MainWindow", "1"))
        self.label_28.setText(_translate("MainWindow", "PET："))
        self.petLab.setText(_translate("MainWindow", "2.6"))
        self.label_37.setText(_translate("MainWindow", "Mask："))
        self.label_29.setText(_translate("MainWindow", "CT："))
        self.ctLab.setText(_translate("MainWindow", "30"))
        self.groupBox_5.setTitle(_translate("MainWindow", "更多信息"))
        self.label_8.setText(_translate("MainWindow", "low"))
        self.label_19.setText(_translate("MainWindow", "high"))
        self.label_4.setText(_translate("MainWindow", "slice\n"
"Index"))
        self.gtSegLabel_2.setText(_translate("MainWindow", "GT"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))

