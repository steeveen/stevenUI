import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from qt.ui.drop.mainUI import  Ui_MainWindow
if __name__ == '__main__':
    app=QApplication(sys.argv)
    mWin=QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mWin)
    mWin.show()
    sys.exit(app.exec_())