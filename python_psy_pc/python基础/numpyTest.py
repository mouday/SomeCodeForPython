#引入包
import numpy
import numpy as np
from numpy import array
#定义数组元素只能有一种类型
arr=numpy.array([1,2,3,4,5])
print(arr)

arr2=np.array([0,1,2,3,4])
print(arr2)

arr1=array([5,6,7,8,9])
print(arr1)

arr3=array([5,6,7,8,"9"])
print(arr3)

arr4=array([5,6,7,8,9.0])
print(arr4)

#print(help(array))

height=np.array([1.73,1.68,1.71,1.89,1.79])
weight=np.array([65.4,59.2,63.6,88.4,68.7])
bmi=weight/height**2
print(weight)
print(height)
print(bmi)

#list与array的区别
list1=[1.73,1.68,1.71,1.89,1.79]
list2=[65.4,59.2,63.6,88.4,68.7]
print(list1+list2)
print(height+weight)

print(weight[0])
print(weight>65)
print(weight[weight>65])
print(type(weight))

#array建立二维数组
np_2d=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(np_2d)
print(np_2d.shape)#2行5列
#print(dir(np_2d))
print(np_2d[0])
print(np_2d[0][2])
print(np_2d[0,2])
print(np_2d[:,1:3])
print(np_2d[1,:])
print(np_2d[1])

print(np.mean(np_2d[0]))#取平均数
print(np.median(np_2d[1]))#取中位数
print(np.corrcoef(np_2d[:,0],np_2d[:,1]))#计算相关性
print(np.std(np_2d[:,0]))#计算标准差

#生产5000条数据
np_weight=np.round(np.random.normal(1.75,0.20,5000),2)
np_height=np.round(np.random.normal(60.32,15,5000),2)
np_city=np.column_stack((np_height,np_weight))

print(np_weight)
print(np_height)
print(np_city)