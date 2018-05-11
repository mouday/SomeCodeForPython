print("---------------")
temp=input("输入一个数：")
guess=int(temp)
if guess==8:
    print("猜对了！")
    print("继续吧！")
else:
    print("猜错了！")
print("游戏结束")
print("------help-----")
print(help(int))
print("------BIF==built-in function-----")
print(dir(__builtins__))
