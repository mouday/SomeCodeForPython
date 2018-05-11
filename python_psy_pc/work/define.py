# -*- coding: cp936 -*-
#判断回文数#
def is_plani(x):
    num = x
    temp = 0
    while x != 0:
        temp = temp * 10 + x % 10
        x = x / 10
    if temp == num:
        return True
    else:
        return False

#判断素数
def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    else:
        return True

x=131
if is_plani(x) and is_prime(x):
    print "ok"
else:
    print "no"
