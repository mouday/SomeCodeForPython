#while True:
#x = float(raw_input("enter a number : "))
import math
count = 0
x = 2
while  count < 50:
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            #print x,"is not a prime"
             break
    else:
        print x,"is a prime"
        count += 1
    x += 1

    #cancel = raw_input("continue?")

    #if cancel == "q":
    #   break
