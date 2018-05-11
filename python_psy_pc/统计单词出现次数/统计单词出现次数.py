#统计字母出现次数.py
def getList(path):
    d={}
    with open(path,"r") as f:
        txt=f.read().replace(" ","")
        for word in txt:
            d[word]=d.get(word,0)+1
    print(d.items())
    #字典无序，需要变成list   
    lst=list(d.items())
    return lst

def sortedbuble(lst):
    # 冒泡排序
    length=len(lst)
    print(length)
    for i in range(length-1):
        for j in range(length-1-i):
            if lst[j][1]>lst[j+1][1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    print(lst)

def main():
    path="Please Dress Me in Red.txt"
    lst=getList(path)
    sortedbuble(lst)
    #sorted
    # 输出排名前三：
    for i,c in sorted(lst,key=lambda x:x[1],reverse=True)[:3]:
        print(i,"count is", c)
                
if __name__=="__main__":
    main()
