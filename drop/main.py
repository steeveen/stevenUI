import tkinter as tki
from PIL import Image,ImageTk
from drop.tk import createAlgPanel
from drop.tk import createMenu
from drop.tk.Com.ImageInfo import  createImageInfoPanel
from drop.tk import  createPatientPanel
from drop.tk import createStatusBar

win = tki.Tk()
win.title("yudanqu")
win.geometry("1300x650+200+50")
createMenu(win)
createPatientPanel(win)
createImageInfoPanel(win)
createAlgPanel(win)


# createToolbar(win)

label1 = tki.Label(win, text="PET", bg="#aaaaaa",width=35,height=1)
label2 = tki.Label(win, text="CT", bg="#aaaaaa",width=35,height=1)
label3 = tki.Label(win, text="Seg",bg="#aaaaaa",width=35,height=1)

# 绝对布局，窗口的变化对位置没有影响
label1.place(x=10,y=20)
label2.place(x=310,y=20)
label3.place(x=610,y=20)




img = Image.open('res\ct.tif')
photo = ImageTk.PhotoImage(img)#在root实例化创建，否则会报错
ctImg = tki.Label(win,image=photo)
ctImg.place(x=9,y=50)


photo2 = ImageTk.PhotoImage( Image.open('res\suv.tif'))#在root实例化创建，否则会报错
suvImg = tki.Label(win,image=photo2)
suvImg.place(x=308,y=50)


photo3 = ImageTk.PhotoImage(Image.open('res\pre.bmp'))#在root实例化创建，否则会报错
preImg = tki.Label(win,image=photo3)
preImg.place(x=608,y=50)

createStatusBar(win)
win.mainloop()