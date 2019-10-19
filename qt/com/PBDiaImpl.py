from qt.com.PbDia import Ui_Dialog
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
class PBDiaImpl(Ui_Dialog,QDialog):
    # def setupUi(self, Dialog):
    #     super().setupUi()
    def __init__(self):
        super().__init__()
        self._translate = QtCore.QCoreApplication.translate

    def setValue(self,value):
        if self.progressBar:
            self.progressBar.setValue(value)
    def setPanel(self,text):
        self.label.setText(self._translate ("Dialog", "<html><head/><body><p align=\"center\">"+text+"</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PBDiaImpl()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

