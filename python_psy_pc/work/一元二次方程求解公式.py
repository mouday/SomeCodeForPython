# -*- coding: cp936 -*-
#一元二次方程求解公式
import math
while True:
    print "aX^2+bX+c=0"
    a=float(raw_input("input a: "))
    b=float(raw_input("input b: "))
    c=float(raw_input("input c: "))
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print "no solution :delta<0"
        elif delta == 0:
            print "root: ",-b / ( 2 * a )
        elif delta>0:
            root=math.sqrt(delta)
            print "root1: ",(-b - root ) / (2 * a)
            print "root2: ",(-b + root) / (2 * a)
        
    else:
        print "no solution :a=0"
    ch=raw_input("continue?(enter/q):")
    if ch =="q":
        print "thank you ! byebye"
        break
    
