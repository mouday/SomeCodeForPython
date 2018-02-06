# 5. Singleton（单例）
# 保证一个类仅有一个实例，并提供一个访问它的全局访问点


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s


    s1 = SingleSpam("A")
    print(id(s1), s1)

    s2 = SingleSpam("B")
    print(id(s2), s2)
    print(id(s1), s1)



