class Test(object):
    name = "a";
    age = 10
    def getName(self):
        return (self.name, Test.age)

    def setName(self, name, age):
        self.name = name
        Test.age = age


t = Test()
print(t.getName())

t.setName("b", 12)
print(t.getName())

t1 = Test()
print(t.getName())
