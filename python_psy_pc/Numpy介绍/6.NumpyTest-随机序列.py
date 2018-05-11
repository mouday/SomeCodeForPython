import numpy as np

#将生成一个处于0~1之间2行4列的随机数序列（不加参数将只返回一个）
a=np.random.rand(2,4)
print("a:\n",a)

#必须有（前两个参数）指定范围，第三个参数用于指定生成的个数
b=np.random.randint(22,55,3)
print("b:\n",b)

#生成标准正态随机数
c=np.random.randn(2,4)
print("c:\n",c)

#从指定可迭代的数组中生成随机数
d=np.random.choice([10,20,30,40,55])
print("d:\n",d)

#生成4个beta分布
e=np.random.beta(1,10,4)
print("e:\n",e)

