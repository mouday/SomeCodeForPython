# 设计模式之简单工厂模式
# http://mp.weixin.qq.com/s/3J0hq3I95iKnbT5YjniZVQ

"""
简单工厂模式: 
专门定义一个 工厂类 来负责创建 产品类 的实例，被创建的产品通常都具有共同的父类。

三个角色:
简单工厂（SimpleProductFactory）角色
抽象产品（Product）角色
具体产品（Concrete Product）角色
"""

# 抽象产品
class Fruit(object):
    def produce(self):
        print("Fruit is prodeced")

# 具体产品
class Apple(Fruit):
    def produce(self):
        print("Apple is produced")

class Banana(Fruit):
    def produce(self):
        print("Banana is produced")

# 简单工厂
class Factory(object):
    def produceFruit(self, fruit_name):
        if fruit_name == "apple":
            return Apple()
        elif fruit_name == "banana":
            return Banana()
        else:
            return Fruit()


if __name__ == '__main__':
    factory = Factory()

    apple = factory.produceFruit("apple")
    apple.produce()

    banana = factory.produceFruit("banana")
    banana.produce()

    fruit = factory.produceFruit("fruit")
    fruit.produce()

"""
Apple is produced
Banana is produced
Fruit is prodeced
"""