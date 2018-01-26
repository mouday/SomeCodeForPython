import os

print(os.getcwd())  #获取当前工作目录，即当前python脚本工作的目录路径
os.chdir(r"D:\CODE\HTML") #改变当前脚本工作目录；相当于shell下cd,相当于shell下cd
print(os.getcwd())
os.chdir(r"D:\CODE\python\python试题\Python17个常用内置模块总结")
print(os.getcwd())

print(os.curdir) #返回当前目录: ('.')
print(os.pardir) #获取当前目录的父目录字符串名：('..')

if not os.path.exists("1/2"):
   os.makedirs("1/2") #可生成多层递归目录
   print("makedirs successful")

os.removedirs("1/2") #若目录为空，则删除
print("removedirs successful")

if not os.path.exists("3"):
    os.mkdir("3")  #生成单级目录；相当于shell中mkdir dirnames
    print("mkdir successful")

os.rmdir("3") #删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
print("rmdir successful")

print(os.listdir()) #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印

if os.path.exists(r"第一级目录\一级目录下的文件.txt"):
    os.remove(r"第一级目录\一级目录下的文件.txt")  #删除一个文件
    print("删除文件成功")

if os.path.exists("1.txt"):
    os.rename("1.txt","2.txt") #重命名文件/目录
    print("重命名成功")

if os.path.exists("2.txt"):
    print(os.stat("2.txt"))#获取文件/目录信息

print(os.sep)#输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.linesep)  #输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
print(os.pathsep)   #输出用于分割文件路径的字符串
print(os.name)  #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
print(os.system("echo 1"))#运行shell命令，直接显示
print(os.environ) #获取系统环境变量

print(os.path.abspath("2.txt")) #返回path规范化的绝对路径

print(os.path.split("1/2.txt"))  #将path分割成目录和文件名二元组返回
print(os.path.dirname("1/2.txt"))  #返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename("1/2.txt"))  #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.exists("1/2.txt"))   #如果path存在，返回True；如果path不存在，返回False

print(os.path.isabs("1/2.txt")) #如果path是绝对路径，返回True
print(os.path.isfile("2.txt"))  #如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir("第一级目录")) #如果path是一个存在的目录，则返回True。否则返回False

print(os.path.join("1","2.txt"))   #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略

import datetime
if not os.path.exists("2.txt"):
    f=open("2.txt","w")
    f.close()
    
stamp=os.path.getatime("2.txt") #返回path所指向的文件或者目录的最后存取时间
print(stamp)
print(datetime.datetime.fromtimestamp(stamp))

stamp=os.path.getmtime("2.txt") #返回path所指向的文件或者目录的最后修改时间
print(stamp)
print(datetime.datetime.fromtimestamp(stamp))

stamp=os.path.getctime("2.txt") 
print(stamp)
print(datetime.datetime.fromtimestamp(stamp))

for i in dir(os):
    print(i)

# 3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】默认topdown=True目录自上而下
for root,dirs,files in os.walk("."):
    for filename in files:
        print(os.path.join(root,filename))
    for directory in dirs:
        print(os.path.join(root,directory))

input("press any key")