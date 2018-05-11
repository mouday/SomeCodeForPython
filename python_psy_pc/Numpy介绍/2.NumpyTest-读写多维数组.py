import numpy as np

a=np.arange(100).reshape(5,10,2)
a.tofile("a.dat",sep=",",format="%d")
# print(a)

b=np.fromfile("a.dat",sep=",",dtype=np.int).reshape(5,10,2)
print(b)

# 写入
# a.tofile(frame,sep='',format='%d')

# frame:文件，字符串
# 数据分割字符串，如果不写，将使用二进制文件存储
# format：写入数据的格式

#读取
# np.fromfile(frame,dtype=float,count=-1,sep='')

# frame：文件
# dtype：读取元素使用的数据类型，默认为float
# count：读文件的个数，默认-1，读取全部
# sep:数据分割字符串，如果是空串，写入文件为二进制。