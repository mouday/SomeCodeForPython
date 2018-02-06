#lambda测试
from functools import reduce
lst=[x for x in range(10)]
print(lst)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

f=lambda x: x*x

lst2=map(f, lst)
print(list(lst2))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

lst3=[1,2,3,4,-1,2,-5,-6]
lst4=sorted(lst3, key=lambda x:abs(x))
print(lst4)
# [1, -1, 2, 2, 3, 4, -5, -6]

lst5=filter(lambda x:x>0,lst3)
print(list(lst5))
# [1, 2, 3, 4, 2]

lst6=reduce(lambda x,y:x+y,lst)
print(lst6)
# 45
