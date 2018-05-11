# 生成器表达式
colors=["red","blue","yellow"]
size=["s","m","l"]

for tshirt in ("%s %s" % (c,s) for c in colors for s in size):
    print(tshirt)