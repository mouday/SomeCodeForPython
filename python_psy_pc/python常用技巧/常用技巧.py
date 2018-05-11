
lst=list(range(10))
print("lst:",lst)

# 匿名函数
lst2=list(map(lambda x: x**2, lst))
print("lst2:",lst2)

# 列表推导式
lst3=[x*x for x in lst]
print("lst3:",lst3)

# 字典推导式
import string
print(string.ascii_uppercase)
dct={i:string.ascii_uppercase[i] for i in lst}
print("dct:",dct)

# 列表解析式
print("直接迭代：")
for i in lst2:
    print(i,end=" ")

print()
print("下标访问：")
for i in range(len(lst2)):
    print(lst2[i],end=" ")

print()
print("返回tuple：")
for index,value in enumerate(lst2):
    print(index,"->",value,end=" ")

# 字典解析
print()
print("key访问")
for i in dct:
    print(dct[i],end=" ")

print("key-value")
for key, value in dct.items():
    print(key,"->",value,end=" ")

#函数作为第一公民
print()
print("函数：")
def a_function(x):
    if isinstance(x, int):
        if 0 <= x < len(string.ascii_uppercase):
            return string.ascii_uppercase[x]
    else:
        return "x not valid"

def b_function(a_list=None, func=None):
    for index, value in enumerate(a_list):
        print(index,"->", func(value))
    return None

b_function(a_list=[1,2,3,"a","d","g",99], func=a_function)