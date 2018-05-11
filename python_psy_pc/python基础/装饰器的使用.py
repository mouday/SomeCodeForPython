def deco(func):
	print("call deco")
	def in_deco():
		print("in deco")
		func()
	return in_deco

#deco(say_hello)-->in_deco
#say_hello=indeco
@deco
def say_hello():
	print("say hello!")

say_hello()