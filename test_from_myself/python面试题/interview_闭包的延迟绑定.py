"""
浅入深谈：一道Python面试题，让我明白了殊途同归，却开始怀疑自己
http://mp.weixin.qq.com/s/bxsjC3cqP2uuwZdgqRWjgQ

Python 的闭包的后期绑定导致的 late binding，
这意味着在闭包中的变量是在内部函数被调用的时候被查找。
所以结果是，当任何 testFun() 返回的函数被调用，在那时，
i 的值是在它被调用时的周围作用域中查找，
到那时，无论哪个返回的函数被调用，for 循环都已经完成了，
i 最后的值是 3，因此，每个返回的函数 testFun 的值都是 3。
因此一个等于 2 的值被传递进以上代码，它们将返回一个值 6 
（比如： 3 x 2）。
"""

def func1():
    temp = [ lambda x: x*i for i in range(4) ]
    print(temp)
    return temp

for f in func1():
    print(f(2))

"""
[
<function func1.<locals>.<listcomp>.<lambda> at 0x021D0618>, 
<function func1.<locals>.<listcomp>.<lambda> at 0x021D05D0>, 
<function func1.<locals>.<listcomp>.<lambda> at 0x021D0588>, 
<function func1.<locals>.<listcomp>.<lambda> at 0x021D0540>
]
6
6
6
6
"""

# 列表生成式
def func2():
    temp = ( lambda x: x*i for i in range(4) )
    print(temp)
    return temp

for f in func2():
    print(f(2))
"""
<generator object func2.<locals>.<genexpr> at 0x021CDDB0>
0
2
4
6
"""

# yield生成器
def func3():
    for i in range(4):
        yield lambda x: x * i

for f in func3():
    print(f(2))

"""
0
2
4
6
"""