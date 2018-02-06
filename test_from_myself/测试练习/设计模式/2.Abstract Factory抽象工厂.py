# 2. Abstract Factory（抽象工厂）
# 提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。 

import random

class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("pet", pet)
        print("speak:", pet.speak())
        print("food:", self.pet_factory.get_food())


class Dog(object):
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"

class Cat(object):
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

class DogFactory(object):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"

class CatFactory(object):
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


def get_factory():
    return random.choice([DogFactory, CatFactory])()


if __name__ == '__main__':
    shop = PetShop()
    for i in range(4):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("="*50)

"""
pet Cat
speak: meow
food: cat food
==================================================
pet Dog
speak: woof
food: dog food
==================================================
pet Dog
speak: woof
food: dog food
==================================================
pet Cat
speak: meow
food: cat food
==================================================
"""