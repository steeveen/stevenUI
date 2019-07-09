from tkinter import *

def createStatusBar(root):

    label = Label(root, text='Huiyan Jiang Lab in Northeastern University', bd=1, relief=SUNKEN, anchor=W)  # anchor left align W -- WEST
    label.pack(side=BOTTOM, fill=X)

    root.mainloop()
