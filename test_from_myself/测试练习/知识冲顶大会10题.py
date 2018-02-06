# 1.运算符的优先级

print(3*1**3)  #3  相当于：3*(1**3)

# 2.小整数池
a = 1
b = 1
print(a is b)  # True

a = 300
b = 300
print(a is b) # True
# 在shell里是False
# [-5, 256]之间的整数，值相同的整数共享一个对象
# is比较内存地址
# ==比较对象的值

# 3.字符串
def foo1(a):
    a = a +"2"
    a = a * 2
    return a

print(foo1("hello"))  # hello2hello2
# 操作符重载
# __add__(+)
# __mul__(*)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

p1=Point(1,2)
p2=Point(3,4)
print(p1+p2) # Point(4, 6)
print(p1*p2) # Point(3, 8)


# 4.浮点数
print(0.3)   # 0.3
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False

# 5.取反操作
print(~5)  # -6
print(~~5)  # 5
print(~~~5)  # -6
# ~按位取反，计算机以补码存储

# 6.布尔
print(bool("Flase"))  # True

# 7.链式比较
print(True == False )  # False
print(False ==False)  # True
print(True == False ==False)  # False
# 相当于  (True == False) and (False == False)

# 8.循环语句
i = 0
while i < 5:
    print(i)
    i += 1
    if i ==3:
        break
else:
    print(0)

"""
0
1
2
"""

# 9.作用域
x = 12 
def f1():
    x = 3
    print(x)

def f2():
    global x  # 没有这个声明报错，local variable 'x' referenced before assignment
    x += 1
    print(x)

f1()
f2()

# 10.python关键字
eval("1-1")  # eval不是关键字，是内建函数
assert(1 == 1)
pass
# nonlocal

import keyword
print(keyword.kwlist)
"""33
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""