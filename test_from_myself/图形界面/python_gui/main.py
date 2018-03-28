"""
参考：
tkinter模块常用参数(python3)
https://www.cnblogs.com/aland-1415/p/6849193.html

Tkinter简易教程
https://www.cnblogs.com/tkinter/p/5629578.html

pyhon之Tkinter实例化学习
https://www.cnblogs.com/kaituorensheng/p/3287652.html

Python基础总结（七）（Tkinter的GUI的程序设计）
https://www.jianshu.com/p/5c7a1af4aa53

An Introduction to Tkinter (Work in Progress)
http://effbot.org/tkinterbook/
"""

import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

root = tk.Tk()  # 生成主窗口
root.title("窗体测试程序")   # 窗体名称
root.geometry("400x300")   # 指定窗体大小

label = ttk.Label(root, text="hello world")
label.pack()

# 事件
def click(event):
    messagebox.showinfo("hello world", "this is a some info")

button1 = tk.Button(root, text="tk-button")
button1.bind("<Button-1>", click)
button1.pack(side=tk.LEFT)

button2 = ttk.Button(root, text="ttk-button")
button2.bind("<Button-1>", click)
button2.pack(side=tk.RIGHT)

root.mainloop()  # 消息循环