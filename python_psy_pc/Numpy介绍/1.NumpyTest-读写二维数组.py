import numpy as np

a=np.arange(20).reshape(4,5)
print(a)
np.savetxt("demo.csv",a,fmt="%d",delimiter=",")

b=np.loadtxt("demo.csv",dtype=np.int,delimiter=",")
print(b)

# 生成数据集
# np.savetxt(frame,array,fmt='%.18e",delimiter=None)

# frame：文件、字符串、或产生器的名字，可以是.gz，.bz2的压缩文件
# arrray：存入文件的NP的数组
# fmt(format):写入文件的格式，如%d,%.2f,%.18e(默认，科学计数法保留18位)
# delemiter:分割字符串，默认是任何空格。

# 读取数据集
# np.loadtxt(frame,dtype=np.float,delimiter=None,inpack=False)

# frame:指定读入的文件来源
# dtype:数据类型，默认为np.float。
# delimiter:分割字符串
# unpack：默认为False读入文件写入一个数组，如果为True，读入属性将分别写入不同变量

# 参考文章：
# Python 数据分析：Numpy 介绍
# http://mp.weixin.qq.com/s/Cg-dqMzsXQhqY85mOjAZIQ
# segmentfault.com/a/1190000011372128