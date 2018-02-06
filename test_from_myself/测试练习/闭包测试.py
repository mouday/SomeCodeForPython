def count():
    fs = []
    for i in range(1, 4):
        def f(m=i):
        	return m*m
        fs.append(f)
    return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())