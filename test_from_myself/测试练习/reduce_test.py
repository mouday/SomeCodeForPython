from functools import reduce  # py3
# 1.map
print(list(map(lambda x: x%3, range(6))))

#列表解析
print([x%3 for x in range(6)])

print(list(map(lambda x, y:(x*y, x+y), [1, 2, 3], [4, 5, 6])))

print(reduce(lambda x, y: x + y, [ 1, 2, 3]))  # 6