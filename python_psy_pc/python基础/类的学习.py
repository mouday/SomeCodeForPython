#coding:utf-8
class Person(object):
	hobby="play"
	def __init__(self,name,age,weight):
		self.name=name
		self._age=age
		self.__weight=weight
	def get_weight(self):
		return self.__weight
	@property
	def get_age(self):
		return self._age
	@classmethod
	def get_hobby(cls):
		return cls.hobby

	def introduction(self):
		print("my name is :%s"%self.name)

class JavaPerson(Person):
	def __init__(self,name,age,weight,language):
		super(JavaPerson,self).__init__(name,age,weight)
		self.language=language
	def introduction(self):
		print("my can language:%s" % self.language)

p1=Person("xiaoming",23,90)
print(dir(p1))
print(p1.__dict__)
print(p1.get_weight())
print(p1.get_age)
#print(p1.get_age())
print(p1.name)
print(Person.get_hobby())
print(p1._age)
#print(p1.__weight)
print(p1._Person__weight)

print("---继承---")
java=JavaPerson("xiaohong",20,100,"java")
print(java.name)
print(dir(java))
print(java.__dict__)
print(java.get_weight())
print(type(java))
print(isinstance(java,JavaPerson))
print(issubclass(JavaPerson,Person))

print("--多态---")
print(p1.introduction())
print(java.introduction())
input()