#1 Python的函数参数传递.py
a=1
def fun1(a):  # 局部变量值传递
    print(a) # 1
    a=2

fun1(a)
print("a=",a) # a= 1

b=[]
def fun2(a): # 引用传递
    a.append(1);

fun2(b)
print("b=",b) # b= [1]