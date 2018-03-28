# 参考
# Pandas入门笔记
# http://blog.csdn.net/weixin_39175124/article/details/73478691

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建序列, 让pandas创建默认整数索引
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
"""
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
"""
# 数据读取

# csv文件读取
# 默认第一行列名，数据从第二行起
# (数据从第一行起header=None)
data = pd.read_csv("data.csv")
print(data)
"""
   id name  age  score
0   1  tom   12     98
1   2  tom   12     98
2   3  tom   12     98
3   4  tom   12     98
4   5  tom   12     98
5   6  tom   12     98
6   7  tom   12     98
7   8  tom   12     98
8   9  tom   12     98
9  10  tom   12     98
"""

# 显示前面几行数据（默认前5行）
print(data.head())
"""
   id name  age  score
0   1  tom   12     98
1   2  tom   12     98
2   3  tom   12     98
3   4  tom   12     98
4   5  tom   12     98
"""
# 读取尾部数据
print(data.tail())
"""
 id name  age  score
5   6  tom   12     98
6   7  tom   12     98
7   8  tom   12     98
8   9  tom   12     98
9  10  tom   12     98
"""

# 显示列名
print(data.columns)
# Index(['id', 'name', 'age', 'score'], dtype='object')

# 显示行号
print(data.index)
# RangeIndex(start=0, stop=10, step=1)

# 显示大小
print(data.shape)
# (10, 4)

# 索引和计算

# 列名默认为字符串(Object)。行的index默认为整数
# 提取行
print(data.loc[3:6])
"""
   id name  age  score
3   4  tom   12     98
4   5  tom   12     98
5   6  tom   12     98
6   7  tom   12     98
"""

# 使用list提取行
print(data[3:6])
"""
   id name  age  score
3   4  tom   12     98
4   5  tom   12     98
5   6  tom   12     98
"""

# 提取列
columns = ["name", "age"]
print(data[columns])
"""
   name  age
0  tom   12
1  tom   12
2  tom   12
3  tom   12
4  tom   12
5  tom   12
6  tom   12
7  tom   12
8  tom   12
9  tom   12
"""

# 列名转为list
print(data.columns.tolist())
# ['id', 'name', 'age', 'score']

print(data.columns.values)
# ['id' 'name' 'age' 'score']

print(data.columns.values.dtype)
# object

# 切片
print(data.loc[3:6][["name", "age"]])
"""
  name  age
3  tom   12
4  tom   12
5  tom   12
6  tom   12
"""

print(data["name"])
"""
0    tom
1    tom
2    tom
3    tom
4    tom
5    tom
6    tom
7    tom
8    tom
9    tom
Name: name, dtype: object
"""

# 取极值
print(data["id"].max())
# 10

# 运算
num = data.shape[0]
age_average = data["id"]/num
print(age_average.head())
"""
0    0.1
1    0.2
2    0.3
3    0.4
4    0.5
Name: id, dtype: float64
"""

# 排序
data.sort_values("id", inplace=False, ascending=False)
print(data.head())