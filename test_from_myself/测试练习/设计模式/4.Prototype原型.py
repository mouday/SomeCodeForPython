# 4. Prototype（原型）
# 用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象

import copy

class Prototype(object):
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


def main():
    class A(object):
        def __str__(self):
            res = []
            for i in self.__dict__:
                res.append(i+" = "+str(self.__dict__[i]))
            return " | ".join(res)

    a = A()
    a.x = 1
    a.y = 1
    prototype = Prototype()
    prototype.register_object("a", a)
    b = prototype.clone("a", a=1, b=2, c=3)

    print(a)
    print(b)


if __name__ == "__main__":
    main()
