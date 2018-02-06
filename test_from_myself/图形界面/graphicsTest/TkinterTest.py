#搜索指定扩展名文件，使用tkinter
__author__="mouday"

from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import os
import fnmatch
import tkinter.scrolledtext as scrolledtext

# 选择路径
def search():
    #判断合法性
    entkw1=entkw.get()
    entType1=entType.get()
    if not (entkw1 and entType1):
        messagebox.showinfo("error","entry can not empty")
        return

    #获取路径
    path=filedialog.askdirectory()
    # print(path)

    fileList=os.walk(path)#遍历文件夹
    listbox.delete(0,END)#清空列表
    for current, dirs,files in fileList:
        # print(current) 当前路径
        # print(dirs) 文件夹
        # print(files)  文件
        #过滤扩展名
        for n in fnmatch.filter(files,entType1):
            filename=os.path.join(current,n)
            filename=filename.replace("/","\\")
            f=open(filename)
            if entkw1 in f.read():
                listbox.insert(END,filename)
            f.close()
def doubleList(event):
    filename=listbox.get(listbox.curselection())
    f=open(filename)
    str1=f.read()
    f.close()

    editWin=Tk()
    editWin.title(filename)
    editWin.geometry("+800+300")

    editText=scrolledtext(editWin, width=120, height=60)
    editText.grid()
    editText.insert(END,str1)

    editWin.mainloop()

win=Tk()#创建窗体
win.title("文件搜索工具")
win.geometry("+600+300")   # geometry n.几何学

#绘制，网格布局
Label(win,text="关键字：").grid(row=0,column=0)
entkw=Entry(win)
entkw.grid(row=0,column=1)

Label(win,text="文件类型：").grid(row=0,column=2)
entType=Entry(win)
entType.grid(row=0,column=3)

btn=Button(win,text="搜 索",command=search)
btn.grid(row=0,column=4)

listbox=Listbox(win,width=80)
listbox.grid(row=1,columnspan=5)
listbox.bind("<Double-Button-1>",doubleList)
win.mainloop()


