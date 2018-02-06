#findValue.py
#在序列中查找字符串，返回下标
def find(sequence,target):
    for i,value in enumerate(sequence):
        if value==target:
           break
    else:#nobreak
        return -1
    return i

def main():
    colors=["red","blue","green","yellow"]
    print(colors)
    print("blue",find(colors,"blue"))
    print("green",find(colors,"green"))
    print("pink",find(colors,"pink"))

main()
