#-*-coding=utf-8-*-
#定义一个计时器，传入一个函数，并返回带计时功能的函数
#定义一个内嵌的包装函数，给传入的函数加上计时功能的包装	
#将包装后的函数返回
import time
def outputsome(func):
	def wrapper():
		print "----begin----"
		func()
		print "----end----"
	return  wrapper

def timeit(func):
	def wrapper():
		start=time.clock()
		func()
		end=time.clock()
		print "used:",end-start
	return wrapper

#@outputsome
#@timeit
def foo():
	print "in fool"
#foo=timeit(foo)
foo=outputsome(timeit(foo))
foo()
