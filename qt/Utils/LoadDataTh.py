from PyQt5.QtCore import QThread,pyqtSignal
import numpy as np
from natsort import natsorted
from glob import glob
from skimage import io as skio
import os
class LoadDataTh(QThread):

    # 自定义一个信号名
    loadDataSignal = pyqtSignal(tuple)  # 定义信号返回的数值类型

    # 构造函数
    def __init__(self):  # model为传入的模型，img为传入的要处理的图片
        super().__init__()
        self.fileName=0
        self.code=0#定义返回的状况，0表示正常

    # 析构函数
    def __del__(self):
        self.work = False
        self.wait()
    def setFileName(self,fileName):
        self.fileName=fileName

    # 该线程主程序
    def run(self):
        ctps = natsorted(glob(os.path.join(self.fileName, '[0-9]*ct.tif')))
        suvps = natsorted(glob(os.path.join(self.fileName, '[0-9]*suv.tif')))
        pres = natsorted(glob(os.path.join(self.fileName, '[0-9]*preMd.bmp')))
        self.ctNp = np.array([skio.imread(i) for i in ctps]).transpose((0, 2, 1))
        self.suvNp = np.array([skio.imread(i) for i in suvps]).transpose((0, 2, 1))
        self.preNp = np.array([skio.imread(i) for i in pres]).transpose((0, 2, 1))
        self.loadDataSignal.emit( ( self.ctNp ,self.suvNp, self.preNp ) )
