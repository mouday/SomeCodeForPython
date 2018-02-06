
# 类中数据的可访问性
class Counter(object):
    public_count = 0  # 类公有变量
    __private_count = 0  # 类私有变量

    def count(self):
        self.public_count += 1  # 实例公有变量
        self.__private_count += 1  # 实例私有变量
        print(self.__private_count)


counter = Counter()  # 实例化
counter.count() # 1
counter.count() # 2
print(counter.public_count) # 访问实例公有变量  2
# print(counter.__private_count)  # 访问实例私有变量  报错

print(counter._Counter__private_count) # 访问实例私有变量  2
print(Counter.public_count) # 访问类公有变量  0 
# print(Counter.__private_count)  # 访问类私有变量 访问出错

"""
单下划线:protected，本身和子类
双下划线:private，本身
头尾双下划线：系统定义特殊方法
"""

