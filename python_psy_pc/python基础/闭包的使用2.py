
def func(fun):
	print("call func")
	def wrapper(*arg):
		print("arg",arg)
		if len(arg)==0:
			return 0
		for val in arg:
			if not isinstance(val,int):
				return 0
		return fun(*arg)
	return wrapper

@func
def my_sum(*arg):
	print("in my_sum")
	return sum(arg)

def my_average(*arg):
	print("in my_average")
	return sum(arg)/len(arg)




# my_sum=func(my_sum)
# my_average=func(my_average)

# print my_sum(1,2,3,4,'1')
# print my_average(1,2,3,4,"0")
print my_sum(1,2,3,4,5)
# print my_average(1,2,3,4,5)