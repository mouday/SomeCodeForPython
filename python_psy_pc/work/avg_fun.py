# -*- coding: cp936 -*-
#求平均值的函数
def avg_com(numlist):
    avg=0
    num_sum=0
    for i in range(0,len(numlist)):
        num_sum=num_sum+numlist[i]
    avg=num_sum/len(numlist)
    return avg

######################################

a=[10,15,20,35,100,200]
#a=[]
print avg_com(a)
