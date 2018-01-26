import random

'''
函数名称：获取一个四位随机码
Parameter：
    None
Return：
    string - 四位随机码
'''
def getCheckCode():
    checkcode=""
    for i in range(4):
        current=random.randrange(0,4)
        if current !=i:
            temp=chr(random.randint(65,90))
        else:
            temp=random.randint(0,9)
        checkcode+=str(temp)
    return checkcode

'''
函数名称：获取一个四位随机码列表
Parameter：
    Number - 随机码个数
Return：
    List - 保存随机码的列表
'''
def getCheckCodeByNum(num):
    lst=[]
    for i in range(num):
        lst.append(getCheckCode())
    return lst

def main():
    print(getCheckCode())
    print(getCheckCodeByNum(50))

if __name__ == '__main__':
    main()