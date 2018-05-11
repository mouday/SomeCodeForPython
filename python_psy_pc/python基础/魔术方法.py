#coding:utf-8
class Programer(object):
	"""docstring for Programer"""
	def __new__(cls,*args,**kwargs):
		print("call new method")
		print (args)
		return super(Programer,cls).__new__(cls,*args,**kwargs)
	
	def __init__(self, name,age):
		print ("call init method")
		self.name = name
		self.age = age
	
	def __eq__(self,other):
		if isinstance(other,Programer):
			if self.age==other.age:
				return True
			else:
				return False
		else:
			raise Exception("the type of object must be Programer!")	

	def __add__(self,other):
		if(isinstance(other,Programer)):
			return self.age+other.age
		else:
			raise Exception("The type of object must be Programer!")

	def __str__(self):
		return "%s is %s years old"%(self.name,self.age)

	def __dir__(self):
		return self.__dict__.keys()

	def __getattribute__(self,name):
		return super(Programer,self).__getattribute__(name)
		# return getattr(self,name)//引起无限递归调用，上限是1000次
		#return self.__dict__[name]
	def __setattr__(self,name,value):
		#setattr(self,name,value)
		self.__dict__[name]=value

		
#if __name__="__main__":
programer=Programer("jam",23)
print(programer.__dict__)
p2=Programer("tom",23)
print(programer==p2)
print(programer+p2)
obj=object()
print(dir(obj))
print(programer)
print(dir(programer))
print(programer.name)



