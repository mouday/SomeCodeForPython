import numpy as np

lst=[[1,3,5],[2,4,6]]
print("lst:")
print(lst)

# np数组定义
np_lst=np.array(lst,dtype=np.float)
print("np_lst:")
print(np_lst)

print("shape:",np_lst.shape)#返回数组的行列
print("ndim:",np_lst.ndim)#返回数组的维数
print("dtype:",np_lst.dtype)#返回数据类型，float默认为64
print("size:",np_lst.size)#大小，6个元素
print("itemsize:",np_lst.itemsize)#np.array每个元素的大小，float64占8个字节
