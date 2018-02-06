salaries=[1,2,3,4,5]
names=["张三","李四","王二","赵六","吴七","王八"]

z=zip(names,salaries)
print(z)  # <zip object at 0x0000000001258248>

print(dict(z)) # {'张三': 1, '吴七': 5, '李四': 2, '赵六': 4, '王二': 3}
print(list(z)) # []

scores=[89,45,56,23,45]
for index,score in enumerate(scores):#返回一个可枚举的对象
    print(index,score)
"""
0 89
1 45
2 56
3 23
4 45
"""
# print(help(zip))