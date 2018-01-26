
# 1、getpass模块详解
import getpass
pwd = getpass.getpass("请输入密码：")  #输入密码不可见
username =getpass.getuser()             #显示当前登录系统用户名;
print(username)
print(pwd)
input("...")

