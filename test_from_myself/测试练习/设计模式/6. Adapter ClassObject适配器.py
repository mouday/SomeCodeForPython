# 6. Adapter Class/Object（适配器）
# 将一个类的接口转换成客户希望的另外一个接口。
# Adapter 模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。

class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "hello"


class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self):
        return "didi"


class Adapter(object):
    # Adapts an object by replacing methods.
    def __init__(self, obj, adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


def main():
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))

    cat = Cat()
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))

    human = Human()
    objects.append(Adapter(human, dict(make_noise=human.speak)))

    car = Car()
    objects.append(Adapter(car, dict(make_noise=car.make_noise)))

    for obj in objects:
        print(obj.name, obj.make_noise())

if __name__ == '__main__':
    main()
