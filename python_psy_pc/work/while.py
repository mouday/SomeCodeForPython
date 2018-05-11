# -*- coding: cp936 -*-
import math
count = 0
while count < 5:
    print count
    if count > 2:
        break
    count += 1

print "********range******"
for i in range(5,11,2):
    print i

print "**************"
print "*******get const e-1*******"
e = 1
for i in range(1,10):    
    e += 1.0/math.factorial(i)
print "value of e is :",e
print "*******get const e-2*******"
e = 1
factorial = 1
for i in range(1,10):
    factorial *=i
    e += 1.0/factorial
print "value of e is :",e

print "*******get const pi-1*******"
pi=0
for i in range(1,10000):
    pi += (-1.0)**(i+1)/(2*i-1)
pi *=4
print "value of pi is :",pi

print "*******get const pi-2*******"
pi=0
sign=1
divisor=1
for i in range(1,10000):
    pi += 4.0* sign/divisor
    sign = -sign   #sign *=-1
    divisor += 2
print "value of pi is :",pi

count=0
for i in range(100,1000):
    if not i % 17:
        count += 1
print "count = ",count

if 4 % 2:
    print 0
else:
    print 1

print "******考拉兹猜想（奇偶 归一）*******"
x = 6
while x !=1:
    if x % 2 == 0:
        x /= 2
    else:
        x = 3 * x + 1
    print x
print "******打印99乘法表*******"
for i in range(1,10):
    for j in range(1,i+1):
        print format(str(i) + "*" + str(j) + "=" + str(i * j),"6"),
    print

print "******鸡兔同笼*******"
for chickens in range(35 + 1):
    for rabbits in range(35 + 1):
             if chickens * 2 +rabbits * 4 == 94 and chickens + rabbits == 35:
                print "chickens : ",chickens
                print "rabbits : ",rabbits
                
