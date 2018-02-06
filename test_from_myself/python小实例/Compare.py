#Compare.py
def cmp(a,b):
    if a>b:
        return 1
    elif a==b:
        return 0
    else:
        return -1

def main():
    print(cmp(1,3))
    print(cmp(1,1))
    print(cmp(3,1))
    print(cmp('axxx','xxb'))
    print(cmp('a','a'))
    print(cmp('b','a'))

if __name__=="__main__":
    main()
