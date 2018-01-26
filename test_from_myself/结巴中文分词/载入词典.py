import jieba

mylist=jieba.cut("李小福是创新办主任也是云计算方面的专家")
print("加载之前：","/".join(mylist))
# 加载之前： 李小福/是/创新/办/主任/也/是/云/计算/方面/的/专家

# 加载自定义词库
jieba.load_userdict("userdict.txt")

mylist=jieba.cut("李小福是创新办主任也是云计算方面的专家")
print("加载之后：","/".join(mylist))
# 加载之后： 李小福/是/创新办/主任/也/是/云计算/方面/的/专家
