#
def is_panlindrom(name):
    low=0
    high=len(name)-1

    while low<high:
        if name[low] !=name[high]:
            return False
        low+=1
        high-=1
    return True

def is_ascending(name):
    p=name[0]
    for c in name:
        if p>c :
            return False
        p=c
    return True

f=open("names.txt","r")

for line in f:
    line = line.strip()
    name=line
    if is_ascending(name):
        print name.title()

f.close()
