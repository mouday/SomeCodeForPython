import numpy as np

lst1=[1,2,3,4]
list1=np.array([1,2,3,4])
print("lst1:\n",lst1)
print("list1:\n",list1)

lst2=[5,6,7,8]
list2=np.array([5,6,7,8])
print("lst2:\n",lst2)
print("list2:\n",list2)

# 列表追加
sum_lst=lst1+lst2
print("sum_lst:\n",sum_lst)

# 数据运算
sum_list=list1+list2
print("sum_list:\n",sum_list)

# 矩阵运算操作
list1_2x2=list1.reshape([2,2])
list2_2x2=list2.reshape([2,2])
print("list1_2x2:\n",list1_2x2)
print("list2_2x2:\n",list2_2x2)

dot_list=np.dot(list1_2x2,list2_2x2)
print("dot_list:\n",dot_list)
