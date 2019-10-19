import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

def createToolbar(root):
    toolframe = tk.Frame(root, height=20, bg='#F7EED6')  # , relief=tk.RAISED)
    frame = tk.Frame(toolframe, bg='#F7EED6')
    ttk.Button(frame, width=20,  command=showdialog).grid(row=0, column=0, padx=1, pady=1, sticky=tk.E)
    ttk.Button(frame, width=20,  command=showdialog).grid(row=0, column=1, padx=1, pady=1, sticky=tk.E)
    ttk.Button(frame, width=20,  command=showdialog).grid(row=0, column=2, padx=1, pady=1, sticky=tk.E)
    frame.pack(side=tk.LEFT)
    toolframe.pack(fill=tk.X)


def showdialog():
    '''各种窗口'''

    res = simpledialog.askstring(title='字符串', prompt='输入一个字符串')
    print(res)

def createMenu(root):
    '''只支持两层嵌套'''
    menus = ['文件', '编辑', '帮助']
    items = [['新建', '打开', '保存', '另存为...', '关闭', '-', '退出'],
             ['撤销', '-', '剪切', '复制', '粘贴', '删除', '选择所有', ['更多...', '数据', '图表', '统计']],
             ['索引', '关于']]
    callbacks = [[showdialog, showdialog, showdialog, showdialog, showdialog, None, showdialog],
                 [showdialog, None, showdialog, showdialog, showdialog, showdialog, showdialog,
                  [showdialog, showdialog, showdialog]],
                 [showdialog, showdialog]]


    menubar = tk.Menu(root)
    for i, x in enumerate(menus):
        m = tk.Menu(menubar, tearoff=0)
        for item, callback in zip(items[i], callbacks[i], ):
            if isinstance(item, list):
                sm = tk.Menu(menubar, tearoff=0)
                for subitem, subcallback in zip(item[1:], callback):
                    if subitem == '-':
                        sm.add_separator()
                    else:
                        sm.add_command(label=subitem, command=subcallback, compound='left')
                m.add_cascade(label=item[0], menu=sm)
            elif item == '-':
                m.add_separator()
            else:
                m.add_command(label=item, command=callback, compound='left')
        menubar.add_cascade(label=x, menu=m)
    root.config(menu=menubar)