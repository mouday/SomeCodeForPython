# self代表类的实例，而非类
class Test(object):
    def prt(self):
        print(self)
        print(self.__class__)

t1 = Test()
t2 = Test()
t1.prt()
"""
<__main__.Test object at 0x000000000120C550>
<class '__main__.Test'>
"""

t2.prt()
"""
<__main__.Test object at 0x000000000120C518>
<class '__main__.Test'>
"""
print("="*50)