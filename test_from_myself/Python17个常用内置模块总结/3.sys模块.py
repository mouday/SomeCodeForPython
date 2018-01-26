# 3、sys模块
import sys

print(dir(sys))
print(sys.argv)  #命令行参数List，第一个元素是程序本身路径
print(sys.version) #获取Python解释程序的版本信息
print(sys.maxsize) #最大的Int值
print(sys.path)  #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform) #返回操作系统平台名称
print(sys.getwindowsversion())

sys.stdout.write("please:")
val=sys.stdin.readlines()[:-1]
print("val",val)

input("press any key...")
sys.exit(0)  #退出程序，正常退出时exit(0)
print("这段话不会被输出")
