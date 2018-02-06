#用字典计数.py

from collections import Counter

def count(lst):
    d={}
    for element in lst:
        if element not in d:
            d[element]=0
        d[element]+=1
    return d

#改进版
def count2(lst):
    d = {}
    for element in lst:
        d[element] = d.get(element, 0) + 1
    return d

# 稍微潮点的方法，但有些坑需要注意，适合熟练的老手。
def count3(lst):
    d = defaultdict(int)
    for element in lst:
        d[element] += 1
    return d

def main():
    colors=["red","green","blue","blue","yellow","yellow","yellow"]
    d=Counter(colors)
    print(d)

main()
