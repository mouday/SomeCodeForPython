# 1、Python与设计模式--单例模式
# https://yq.aliyun.com/articles/70418

# 单例模式：保证一个类仅有一个实例，并提供一个访问它的全局访问点。

import threading
import time

# 抽象单例
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# 总线
class Bus(Singleton):
    lock = threading.RLock() 
    def sendData(self, data):
        Bus.lock.acquire()
        time.sleep(3)
        print("sendData:", data)
        Bus.lock.release()

# 线程对象
class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)

if __name__ == '__main__':
    for i in range(3):
        print("run %s"%(i))
        my_entity = VisitEntity()
        my_entity.setName("entity_" + str(i))
        my_entity.start()

"""
run 0
run 1
run 2
sendData: entity_0
sendData: entity_1
sendData: entity_2
"""