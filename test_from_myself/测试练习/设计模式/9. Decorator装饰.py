# 9. Decorator（装饰）
# 动态地给一个对象添加一些额外的职责。
# 就增加功能来说，Decorator 模式相比生成子类更为灵活。 

class foo(object):
    def f1(self):
        print("f1")

    def f2(self):
        print("f2")


class foo_decorator(object):
    def __init__(self, decoratee):
        self.decoratee = decoratee

    def f1(self):
        print("decorated f1")
        self.decoratee.f1()

    def __getattr__(self, name):
        return getattr(self.decoratee, name)


u = foo()
v = foo_decorator(u)
v.f1()
v.f2()

"""
decorated f1
f1
f2
"""
