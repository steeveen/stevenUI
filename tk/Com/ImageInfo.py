import tkinter as tk
def createImageInfoPanel(root):

    label1 = tk.Label(root, text="坐标信息：", width=15, height=1)
    label2 = tk.Label(root, text="x:", width=4, height=1)
    label3 = tk.Label(root, text="004",bg='#aaaaaa' ,width=4, height=1)
    label4 = tk.Label(root, text="y:", width=4, height=1)
    label5 = tk.Label(root, text="005",bg='#aaaaaa', width=4, height=1)
    label6 = tk.Label(root, text="z:", width=4, height=1)
    label7= tk.Label(root, text="006",bg='#aaaaaa', width=4, height=1)

    label1.place(x=880, y=200)
    label2.place(x=950, y=240)
    label3.place(x=980, y=240)
    label4.place(x=1010, y=240)
    label5.place(x=1040, y=240)
    label6.place(x=1070, y=240)
    label7.place(x=1100, y=240)


    label8 = tk.Label(root, text="CT:", width=4, height=1)
    label9 = tk.Label(root, text="100", bg='#aaaaaa', width=4, height=1)
    label10 = tk.Label(root, text="SUV:", width=4, height=1)
    label11= tk.Label(root, text="2.4", bg='#aaaaaa', width=4, height=1)
    label12= tk.Label(root, text="Seg:", width=4, height=1)
    label13= tk.Label(root, text="001", bg='#aaaaaa', width=4, height=1)


    label8.place(x=950, y=265)
    label9.place(x=980, y=265)
    label10.place(x=1010, y=265)
    label11.place(x=1040, y=265)
    label12.place(x=1070, y=265)
    label13.place(x=1100, y=265)

    btn1=tk.Button(root,text='上一页',bg='#bbbbbb' ,width=10, height=1)
    btn2=tk.Button(root,text='下一页',bg='#bbbbbb', width=10, height=1)

    btn1.place(x=950,y=300)
    btn2.place(x=1060,y=300)

