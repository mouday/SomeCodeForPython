import os
import shutil  #文件拷贝使用
print(os.name)
#print(os.environ)
print(os.path.abspath("."))#当前路径

deskTop=r"C:\Users\PSY\Desktop\folder"
dirpath=os.path.join(deskTop,"test")

#文件夹操作
if not os.path.isdir(dirpath):
	os.mkdir(dirpath)
	print("创建文件完成")
else:
	print("文件已存在")

if os.path.isdir(dirpath):
	os.rmdir(dirpath)
	print("删除文件完成")
else:
	print("文件不存在")

filepath=os.path.join(deskTop,"test.txt")
newName=os.path.join(deskTop,"newtest.txt")
dstName=os.path.join(deskTop,"dsttest.txt")

dirname=os.path.split(filepath)[0]
filename=os.path.split(filepath)[1]
file=os.path.splitext(filename)[0]
fileext=os.path.splitext(filename)[1]
print(dirname)
print(filename)
print(file)
print(fileext)

print(filepath)
if os.path.isfile(filepath):
	os.rename(filepath,newName)
	print("重命名完成")
else:
	print("文件不存在")

if os.path.isfile(newName):
	shutil.copyfile(newName,dstName)
	print("文件拷贝完成")

if os.path.isfile(newName):
	os.remove(newName)
	print("文件删除成功")
else:
	print("文件不存在")

mylist=[x for x  in os.listdir(deskTop)]
print(mylist)
#过滤文件
mydir=[x for x in os.listdir(deskTop) if os.path.isdir(os.path.join(deskTop,x))]
print(mydir)
l=[x for x in os.listdir(deskTop) if os.path.isfile(os.path.join(deskTop,x)) and os.path.splitext(os.path.join(deskTop,x))[1]==".txt"]
print(l)