#property_test.py

class Student(object):

	def __init__(self,name,age):
		self._name=name
		self._age=age

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,value):
		self._name=value


def main():
	s=Student()
	s.name="java"
	print(s.name)

main()