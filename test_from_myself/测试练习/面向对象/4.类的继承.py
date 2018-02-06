# 类的继承
"""
面向对象的编程好处之一是代码重用，
在python中继承中的一些特点：
1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。
区别在于类中调用普通函数时并不需要带上self参数
3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，
它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
"""
# 父类
class Parent(object):
    parent_attr = 10
    def __init__(self):
        print("Parent init")

    def parent_method(self):
        print("parent_method")

    def method(self):
        print("method of parent")

    def set_attr(self, attr):
        Parent.parent_attr = attr

    def get_attr(self):
        return Parent.parent_attr

# 子类
class Child(Parent):
    def __init__(self):
        print("Child init")

    def child_method(self):
        print("Child_method")

    def method(self):  # 重写父类方法
        print("method of child")

child = Child()        # 实例化子类  Child init
child.child_method()   # 调用子类的方法  Child_method
child.parent_method()  # 调用父类方法  parent_method
child.method()         # 子类调用重写方法  method of child
child.set_attr(20)     # 设置属性值
print(child.get_attr()) # 获取属性值  20

# 判断A是B的子类
print(issubclass(Child, Parent))  # True

# 判断A是B的实例
print(isinstance(child, Child))  # True