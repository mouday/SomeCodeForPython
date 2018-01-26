import itertools

# “无限”迭代器

# 创建一个无限的迭代器，代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
def testCount():
    natuals=itertools.count(1)
    for i in natuals:
        print(i)
# testCount()


# 传入的一个序列无限重复下去
def testCycle():
    cs=itertools.cycle("ABC")
    for i in cs:
        print(i)
# testCycle()

# 责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
def testRepeat():
    r=itertools.repeat("A",10)
    for n in r:
        print(n)

# testRepeat()

# 打印出1到10
# 通过takewhile()等函数根据条件判断来截取出一个有限的序列
def testTakewhile():
    natuals=itertools.count(1)#从1开始
    ns=itertools.takewhile(lambda x:x<=10, natuals)
    for n in ns:
        print(n)

# testTakewhile()

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
def testchain():
    cs=itertools.chain("ABC","XYZ")
    for c in cs:
        print(c)
# testchain()

def testGroupby():
    for key,group in itertools.groupby("AAAaaABBBCCCDDD"):
        print(key,list(group))
# testGroupby()

def testGroupbyupper():
    for key,group in itertools.groupby("AAaAABBbCCCddDDD",lambda x:x.upper()):
        print(key,list(group))
# testGroupbyupper()

# imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
def testimap():
    for i in map(lambda x,y:x*y,[10,20,30],itertools.count(1)):
        print(i)

testimap()
