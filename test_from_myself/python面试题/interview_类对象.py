
# 1、__call__函数
class Foo():
    def __init__(self):
        print("Foo-init")

    def __call__(self):
        print("Foo-call")

f = Foo()
f()  # 重载了括号运算符
"""
Foo-init
Foo-call
"""

# 2、类装饰器
class Decorator():
    def __init__(self, func):
        print("Decorator-init")
        self.fun = func

    def __call__(self, args1, args2):
        print("Decorator-call")
        self.fun(args1, args2)

@Decorator
def add(a, b):
    print("a+b:", a+b)

# add(1, 2)
"""
Decorator-init
Decorator-call
a+b: 3
"""

# 3、__new__和__init__
class MyTuple(tuple):
    def __init__(self, seq):
        print("MyTuple-init")
        print("self:", self)
        # takes no parameters
        super(MyTuple, self).__init__()

    def __new__(cls, seq):
        print("MyTuple-new")
        # 过滤
        g = [i for i in seq if isinstance(i ,int)]
        # 返回对象：self
        return super(MyTuple, cls).__new__(cls, g)  

    

t = MyTuple([1, 2, "-1"])
print(type(t), t)
"""
MyTuple-new
MyTuple-init
self: (1, 2)
<class '__main__.MyTuple'> (1, 2)
"""

# 4、__set__,__get__,__delete__
# 描述符 : 允许你自定义在引用一个对象属性时应该完成的事情
# __set__:在设计属性的时候被调用
# __get__:在读取属性的时候被调用
# __delete__:在删除属性的时候被调用
class Descriptor():
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

    def __delete__(self, instance):
        print("delete")

class A():
    x = Descriptor()

a = A()
a.x
a.x = 1
del a.x
"""
get
set
delete
"""

# 5、描述符实例：属性做类型检查
class Attr():
    def __init__(self, name, name_type):
        self.name = name
        self.name_type = name_type

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.name_type):
            raise TypeError("expected an {}".format(self.name_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# p.name='jack' #名字必须是str 
# p.age=18 #年龄必须是int
class Person():
    name = Attr("name", str)
    age = Attr("age", int)

p=Person()
p.name= "Tom"
p.age = 123

"""
>参考：
>
>[面试Python如果你说出这几招，让你瞬间牛叉](http://mp.weixin.qq.com/s/_fsh6E-8WjFTdoMZ8aH4RA)
"""