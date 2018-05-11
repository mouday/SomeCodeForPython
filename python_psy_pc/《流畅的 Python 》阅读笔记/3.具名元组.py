# 具名元组
# 元组经常被作为 不可变列表 的代表. 
# 经常只要数字索引获取元素, 
# 但其实它还可以给元素命名:
from collections import namedtuple
City=namedtuple("City","name country population coordinates")
tokyo=City("Tokyo","JP",36.933,(35.689722,139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])