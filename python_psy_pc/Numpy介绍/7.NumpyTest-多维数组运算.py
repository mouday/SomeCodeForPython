import numpy as np

#得到step为2的range序列
a=np.arange(1,11,2)
print("a:\n",a)

# reshape函数，对数组结构重定义
b=np.arange(1,11).reshape(2,5)#（5可以缺省为-1）
print("b:\n",b)

#自然指数操作
c=np.exp(b)
print("c:\n",c)

# sqrt、log、sin、sum、max
d=np.sqrt(b)
print("d:\n",d)

e=np.log(b)
print("e:\n",e)

f=np.sin(b)
print("f:\n",f)

g=np.sum(b)
print("g:\n",g)

h=np.max(b)
print("h:\n",h)

# 三维数组
lst=np.array([
    [[1,2,3,4],[4,5,6,7]],
    [[7,8,9,10],[10,11,12,13]],
    [[14,15,16,17],[18,19,20,21]]
    ])

lst_sum=lst.sum()
print("lst_sum:\n",lst_sum)

# 参数axis 设置求和的深入维度
lst_sum0=lst.sum(axis=0)
print("lst_sum0:\n",lst_sum0)
#22=1+7+14；25=2+8+15

lst_sum1=lst.sum(axis=1)
print("lst_sum1:\n",lst_sum1)
#5=1+4；7=2+5

lst_sum2=lst.sum(axis=2)
print("lst_sum2:\n",lst_sum2)
#10=1+2+3+4；22=4+5+6+7