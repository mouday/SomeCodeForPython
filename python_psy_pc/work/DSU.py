def dsu(words):
    t=[]
    for w in words:
        t.append((len(w),w))
        
    t.sort(reverse=True)

    res=[]
    for length,word in t:
        res.append(word)

    return res

words=["aaa","bbbbbb","a","rr"]
#print dsu(words)

words.sort(key=lambda x : len(x),reverse=True)
print words
