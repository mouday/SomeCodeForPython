import jieba
import time
g = jieba.cut('给我播放一年级语文上册第一课')
print(type(g))
print(g)
print("----------------")
for n in g:
   print (n)
print("----------------")
end2 = time.time()

print(' '.join(g))

