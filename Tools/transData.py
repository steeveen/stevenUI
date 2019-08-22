# -*- coding: utf-8 -*-
from natsort import natsorted
from glob import glob
import os
import shutil
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
 @Author = 'steven'   @DateTime = '2019/7/9 18:44'
'''
ip=r'F:\result'
op=r'E:\pyWorkspace\dataset'
os.mkdir(op) if not os.path.exists(op) else None

ctps=natsorted(glob(os.path.join(ip,'*','col*ct.tif')))
suvps=natsorted(glob(os.path.join(ip,'*','col*suv.tif')))
gtps=natsorted(glob(os.path.join(ip,'*','col*gt.bmp')))
preps=natsorted(glob(os.path.join(ip,'*','col*preMd.bmp')))

for l in [ctps,suvps,gtps,preps]:
    for i in l:
        patientId=i.split('\\')
        opDir=os.path.join(op,patientId[-2])
        os.mkdir(opDir) if not os.path.exists(opDir) else None
        shutil.copy(i,os.path.join(opDir,patientId[-1]))