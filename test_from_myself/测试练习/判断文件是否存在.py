#判断文件是否存在.py
import os
#文件存在
print(os.path.exists(r"C:\Users\PSY\Desktop\folder\test.txt"))
#文件夹存在
print(os.path.exists(r"C:\Users\PSY\Desktop\folder\test"))
#检查文件存在
print(os.path.isfile(r"C:\Users\PSY\Desktop\folder\test.txt"))
os