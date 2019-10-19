import tkinter as tk
from PIL import ImageTk
def createPatientPanel(root):
    label1 = tk.Label(root, text="患者信息", width=15, height=1)
    label2 = tk.Label(root, text="姓名：", width=15, height=1)
    label3 = tk.Label(root, text="性别：",width=15, height=1)
    label4 = tk.Label(root, text="出生日期：", width=15, height=1)
    label5 = tk.Label(root, text="检查日期：", width=15, height=1)

    label22 = tk.Label(root, text="XXX", bg="#aaaaaa", width=10, height=1)
    label32 = tk.Label(root, text="男", bg="#aaaaaa", width=10, height=1)
    label42 = tk.Label(root, text="1970-01-01", bg="#aaaaaa", width=10, height=1)
    label52 = tk.Label(root, text="2019-07-01", bg="#aaaaaa", width=10, height=1)

    # 绝对布局，窗口的变化对位置没有影响
    label1.place(x=880, y=20)
    label2.place(x=950, y=60)
    label3.place(x=950, y=85)
    label4.place(x=950, y=110)
    label5.place(x=950, y=135)


    label22.place(x=1050, y=60)
    label32.place(x=1050, y=85)
    label42.place(x=1050, y=110)
    label52.place(x=1050, y=135)
