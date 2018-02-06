# 10. Facade（外观）
# 为子系统中的一组接口提供一个一致的界面，
# Facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。

class T1(object):
    def run(self):
        print("in test1")

class T2(object):
    def run(self):
        print("in test2")

class T3(object):
    def run(self):
        print("in test3")


class TestRunner(object):
    def __init__(self):
        self.t1=T1()
        self.t2=T2()
        self.t3=T3()
        self.ts = [i for i in (self.t1, self.t2, self.t3)]

    def run(self):
        [i.run() for i in self.ts]


if __name__ == '__main__':
    runner = TestRunner()
    runner.run()
    """
    in test1
    in test2
    in test3
    """