# 深拷贝deepcopy与浅拷贝copy

# Python中的对象之间赋值时是按引用传递的，如果需要拷贝对象，需要使用标准库中的copy模块。

# 1. copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。
# 2. copy.deepcopy 深拷贝 拷贝对象及其子对象

import copy

a=[1,2,3,['a','b']]  #原始对象

b=a     #对象赋值，引用传递

c=copy.copy(a) #对象拷贝，浅拷贝

d=copy.deepcopy(a) #对象拷贝，深拷贝

a.append(5)  #修改对象a

a[3].append('c')  #修改对象a中的['a', 'b']数组对象

print(a)
print(b)
print(c)
print(d)

"""
[1, 2, 3, ['a', 'b', 'c'], 5]
[1, 2, 3, ['a', 'b', 'c'], 5]
[1, 2, 3, ['a', 'b', 'c']]
[1, 2, 3, ['a', 'b']]
"""