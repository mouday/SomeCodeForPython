'''
python3 起，filter 函数返回的对象从列表改为 filter object（迭代器）
def is_odd(n):
    return n % 2 == 1
 
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)
'''
a=filter(lambda x:x%2==1,range(10))
b=[x for x in a]
print(b) # [1, 3, 5, 7, 9]