#lean py test
a=1
b=3
print("a=",a,"b=",b)

a,b=b,a
print("a=",a,"b=",b)

def fib(max):
    n, a, b=0,0,1
    while n< max:
        print(b)
        a,b=b,a+b
        n=n+1
    return "done"
fib(10)
