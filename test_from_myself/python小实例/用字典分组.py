#用字典分组.py
#按照长度分组
def splitElements(lst):
    d={}
    for element in lst:
        key=len(element)
        if key not in d:
            d[key]=[]
        d[key].append(element)
    return d

def main():
    names=["a","b","c","d","a","a","aa","bb","dd","ccc","ddd"]
    d=splitElements(names)
    print(d)
    for k in d:
        print(k,"-->",d[k])

main()
