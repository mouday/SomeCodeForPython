def getnum():
    for i in range(10):
        yield i

def main():
    f=getnum()
    for i in range(10):        
        print (f.__next__())


def yieldTest():
    i=1
    yield i+1


for i in range(5):
    print(yieldTest())