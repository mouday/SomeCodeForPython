f=open("emma.txt","r")
dic={}
for line in f:
    words=line.strip().split()
    for word in words:
        if word in dic:
            dic[word] +=1
        else:
            dic[word]=1
lst=[]

for word,count in dic.items():
    lst.append((count,word))

lst.sort(reverse=True)
for freq,word in lst[:10]:
    print word,freq
    
f.close()
