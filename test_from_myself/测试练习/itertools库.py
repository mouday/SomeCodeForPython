
import itertools

def print_info(obj: "iter object") -> "print_info":
    print(obj)
    print(type(obj))
    print(list(obj))

# help(print_info)  
# print_info(obj:'iter object') -> 'print_info'

# range对象
r = range(10)
print_info(r)
"""
range(0, 10)
<class 'range'>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# 累加
x = itertools.accumulate(range(10))
print(x)# <itertools.accumulate object>
print(list(x))  # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

# 产生多个列表和迭代器的(积)
x = itertools.product("ABC", range(3))
print(list(x))
"""
[('A', 0), ('A', 1), ('A', 2), ('B', 0), 
('B', 1), ('B', 2), ('C', 0), ('C', 1), ('C', 2)]
"""

# 连接多个列表或者迭代器
x = itertools.chain(range(3), range(4), [6, 7, 8])
print(x) # <itertools.chain object>
print(list(x))# [0, 1, 2, 0, 1, 2, 3, 6, 7, 8]

# 求列表或生成器中指定数目的元素不重复的所有组合
x = itertools.combinations(range(4), 3)
print(type(x))  # <class 'itertools.combinations'>
print(list(x))
# [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]

# 允许重复元素的组合
x = itertools.combinations_with_replacement("ABC", 2)
print(list(x))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

# 产生指定数目的元素的所有排列(顺序有关)
x = itertools.permutations(range(4), 3)
print(list(x))
"""
[(0, 1, 2), (0, 1, 3), (0, 2, 1), (0, 2, 3), 
(0, 3, 1), (0, 3, 2), (1, 0, 2), (1, 0, 3), 
(1, 2, 0), (1, 2, 3), (1, 3, 0), (1, 3, 2), 
(2, 0, 1), (2, 0, 3), (2, 1, 0), (2, 1, 3), 
(2, 3, 0), (2, 3, 1), (3, 0, 1), (3, 0, 2), 
(3, 1, 0), (3, 1, 2), (3, 2, 0), (3, 2, 1)]
"""

# 按照真值表筛选元素
x = itertools.compress(range(5), (True, False, False, True, True))
print(list(x))  # [0, 3, 4]

# 无限计数器,可以指定起始位置和步长
x = itertools.count(start=20, step=-1)
print(list(itertools.islice(x, 0, 10, 1)))
# [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

# 无限循环指定的列表和迭代器
x = itertools.cycle("ABC")
print(list(itertools.islice(x, 0, 10, 1)))
# ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']


# 保留对应真值为False的元素
x = itertools.filterfalse(lambda e : e < 5, (1, 5, 3, 6, 9, 4))
print(list(x))  # [5, 6, 9]

# 按照分组函数的值对元素进行分组
x = itertools.groupby(range(10), lambda e: e < 5 or e > 8)
for condition, numbers in x:
    print(condition, list(numbers))
"""
True [0, 1, 2, 3, 4]
False [5, 6, 7, 8]
True [9]
"""

# 对迭代器进行切片
x = itertools.islice(range(10), 0, 9, 2)
print(list(x))  # [0, 2, 4, 6, 8]


# 简单的生成一个拥有指定数目元素的迭代器
x = itertools.repeat(0, 5)
print(list(x))  # [0, 0, 0, 0, 0]


# 按照真值函数丢弃掉列表和迭代器前面的元素
x = itertools.dropwhile(lambda e: e < 5, range(10))
print(list(x))  # [5, 6, 7, 8, 9]

# 与dropwhile相反，保留元素直至真值函数值为假。
x = itertools.takewhile(lambda e: e < 5, range(10))
print(list(x))
# [0, 1, 2, 3, 4]

# 生成指定数目的迭代器
x = itertools.tee(range(10), 2)
for letters in x:
    print(list(letters))

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# 类似于zip，不过已较长的列表和迭代器的长度为准
x = itertools.zip_longest(range(3), range(5))
y = zip(range(3), range(5))
print(list(x))
print(list(y))
"""
[(0, 0), (1, 1), (2, 2), (None, 3), (None, 4)]
[(0, 0), (1, 1), (2, 2)]
"""

# 类似map
x = itertools.starmap(str.islower, "asdfgDFASDF")
y = map(str.islower, "asdfgDFASDF")

print(list(x))
print(list(y))
"""
[True, True, True, True, True, False, False, False, False, False, False]
[True, True, True, True, True, False, False, False, False, False, False]
"""

# help(itertools)
"""
    Infinite iterators: 无限迭代器
    count(start=0, step=1) --> start, start+step, start+2*step, ...
    cycle(p) --> p0, p1, ... plast, p0, p1, ...
    repeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times
    
    Iterators terminating on the shortest input sequence:
    accumulate(p[, func]) --> p0, p0+p1, p0+p1+p2
    chain(p, q, ...) --> p0, p1, ... plast, q0, q1, ... 
    chain.from_iterable([p, q, ...]) --> p0, p1, ... plast, q0, q1, ... 
    compress(data, selectors) --> (d[0] if s[0]), (d[1] if s[1]), ...
    dropwhile(pred, seq) --> seq[n], seq[n+1], starting when pred fails
    groupby(iterable[, keyfunc]) --> sub-iterators grouped by value of keyfunc(v)
    filterfalse(pred, seq) --> elements of seq where pred(elem) is False
    islice(seq, [start,] stop [, step]) --> elements from
           seq[start:stop:step]
    starmap(fun, seq) --> fun(*seq[0]), fun(*seq[1]), ...
    tee(it, n=2) --> (it1, it2 , ... itn) splits one iterator into n
    takewhile(pred, seq) --> seq[0], seq[1], until pred fails
    zip_longest(p, q, ...) --> (p[0], q[0]), (p[1], q[1]), ... 
    
    Combinatoric generators:
    product(p, q, ... [repeat=1]) --> cartesian product
    permutations(p[, r])  排列
    combinations(p, r)  组合
    combinations_with_replacement(p, r)

"""

# 参考：
# 《相见恨晚的 itertools 库》
# http://mp.weixin.qq.com/s/Rb5aYWA7NYOi1eckGtakuQ

