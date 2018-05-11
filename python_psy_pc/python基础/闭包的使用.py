def setPassLine(val):
	passLine=val
	def func(score):
		if(score>=passLine):
			print("pass")
		else:
			print("fail")
	return func

f100=setPassLine(60)
f100(59)
print f100.__closure__
print type(f100)
f150=setPassLine(90)
f150(89)
f150(91)