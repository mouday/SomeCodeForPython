# -*- coding: cp936 -*-
print "*********递归*********"
def p(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * p(n-1)

print p(3)

print "*********斐波那契*********"
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
for i in range(1,10):
    print fib(i)

print "*********汉诺塔*********"
count = 0
def hanoi(x,A,B,C):
    global count
    if x == 1:
        print "1move",x ,"from" ,A, "to",C
        count += 1
    else:
        hanoi(x - 1,A,C,B)
        print "2move",x ,"from",A, "to",C
        count += 1
        hanoi(x - 1,B,A,C)
       

hanoi(3,"left","mid","right")
print "count : ",count
