"""
10个Python面试常问的问题
原文链接：https://mp.weixin.qq.com/s/NIfaEOplupmvryo_SntFAw
"""

# 1.类继承
def class_test():
    class A(object):
        def show(self):
            print("class A")

        def hello(self):
            print("hello")

    class B(A):
        def show(self):
            print("class B")

    b =B()
    b.show()
    b.hello()
    # 调用类A的show方法
    b.__class__ = A
    b.show()  
    # __class__方法指向了类对象，只用给他赋值类型A，
    # 然后调用方法show，但是用完了记得修改回来。
    """OUT
    class B
    hello
    class A
    """

# 2.方法对象
def call_test():
    class A(object):
        def __init__(self, a, b):
            self._a = a
            self._b = b

        def myprint(self):
            print("a =", self._a, "b =", self._b)

        # 为了能让对象实例能被直接调用，需要实现__call__方法
        def __call__(self, num):
            print("call:", num)

    a = A(1, 2)
    a.myprint()
    a(11)
    """OUT:
    a = 1 b = 2
    call: 11
    """

# 3.new和init
def new_test():
    class A(object):
        def __init__(self):
            print("A init")

        def foo(self):
            print("A foo")

    class B(object):
        def __init__(self, a):
            print("B init")

        # 使用__new__方法，可以决定返回那个对象，也就是创建对象之前，
        # 这个可以用于设计模式的单例、工厂模式。
        # __init__是创建对象是调用的。
        def __new__(cls, a):
            print("B new")
            if a>10:
                return super(B, cls).__new__(cls)
            return A()

        def foo(self):
            print("B foo")

    b1 = B(5)
    b1.foo()

    b2 = B(20)
    b2.foo()
    """OUT:
    B new
    A init
    A foo
    B new
    B init
    B foo
    """

# 4.list和dict生成式
def list_test():
    lst = [i for i in range(5)]
    print(lst)  # [0, 1, 2, 3, 4]

    list1 = [i for i in lst if i >2]
    print(list1)  # [3, 4]

    list1 = [i**2 for i in lst if i >2]
    print(list1)  # [9, 16]

    dict1 = {x: x**2 for x in (2, 4, 6)}
    print(dict1)  # {2: 4, 4: 16, 6: 36}

    dict2 = {x: "item" + str(x**2) for x in (2, 4, 6)}
    print(dict2)  # {2: 'item4', 4: 'item16', 6: 'item36'}

    set1 = {x for x in "hello world" if x not in "low level"}
    print(set1)  # {'r', 'h', 'd'}

# 5.全局和局部变量
def global_test():
    num = 10
    def f1():
        num = 20
        print("f1")

    def f2():
        print(num)

    f2()  # 10    
    f1()  # f1
    f2()  # 10

    # num不是个全局变量，所以每个函数都得到了自己的num拷贝，
    # 如果你想修改num，则必须用global关键字声明。
    global n
    n = 10
    def f3():
        global n  # 说明使用全局变量a，不说明则是局部变量
        n = 30

    def f4():
        print(n)

    f4()  # 10
    f3()
    f4()  # 30

# 6.交换两个变量的值
def swap_test():
    a = 1 
    b= 2
    print("a =", a, "b =", b)
    a, b = b, a  # 一行代码交换两个变量值
    print("a =", a, "b =", b)

# 7.默认方法
def default_test():
    class A(object):
        def __init__(self):
            print("init")

        # 当fn1方法传入参数时，我们可以给mydefault方法增加一个*args不定参数来兼容。
        def mydefault(self, *args):
            print("mydefault",args[0])

        # 方法__getattr__只有当没有定义的方法调用时，才调用他。
        def __getattr__(self, name):
            print("name:", name)
            return self.mydefault

    print("===========")
    a = A()
    a.f1(0)
    a.f2(1, 2)
    a.f3(2, 3, 4)
# default_test()
"""
init
name: f1
mydefault 0
name: f2
mydefault 1
name: f3
mydefault 2
"""

# 8.包管理
#一个包里有三个模块，mod1.py, mod2.py, mod3.py，
#但使用from demopack import *导入模块时，只有mod1、mod3被导入了。
#__all__ = ["mod1", "mod3"]

from demopack import *   # import * only allowed at module level
def packge_test():
    pass

# 9.闭包
# 函数，接收整数参数n，返回一个函数，
# 函数的功能是把函数的参数和n相加并把结果返回。
def closure_test():
    def add(num):
        def add_num(val):
            return num + val
        return add_num
    a = add(5)
    print(a(5))

# 10.性能
def performance_test():
    import time
    def str_test(num):
        start = time.time()
        string = ""
        for i in range(num):
            string += str(i)
        end = time.time()
        print("str_time:", end - start)
        # print(string)

    def append_test(num):
        start = time.time()
        lst=[]
        for i in range(num):
            lst.append(str(i))
        end = time.time()
        print("append_time:", end - start)
        # print("".join(lst))

    num = 1000000
    str_test(num)  # str_time: 1.926110029220581
    append_test(num)  # append_time: 0.3060173988342285
    # str_time / append_time = 6.29411934275007
    # mygod!!! 时间相差6倍
    # python的str是个不可变对象，每次迭代，都会生成新的str对象来存储新的字符串
    # num越大，创建的str对象越多，内存消耗越大。

def main():
    performance_test()

if __name__ == '__main__':
    main()