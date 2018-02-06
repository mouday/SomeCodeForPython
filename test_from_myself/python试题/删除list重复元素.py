# 请写出一段python代码实现删除一个list里边的重复元素

def deleteRepeatElement1(lst):
    tempList=[]

    for e in lst:
        if e not in tempList:
            tempList.append(e)

    return tempList

def deleteRepeatElement2(lst):
    return list(set(lst))

def main():
    lst=[1,2,3,4,5,1,2,3,4,5]
    lst=deleteRepeatElement2(lst)
    print(lst)
    # [1, 2, 3, 4, 5]

if __name__ == '__main__':
    main()
