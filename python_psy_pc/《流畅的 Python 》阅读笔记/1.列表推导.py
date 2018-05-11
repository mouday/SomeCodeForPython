# 把一个字符串变成unicode的 码位列表

# way 1:
symbols = '$¢£¥€¤'

codes=[]
for symbol in symbols:
    codes.append(ord(symbol))

print("codes:",codes)

# way2:使用列表推导
codes2=[ord(symbol) for symbol in symbols]
print("codes2:",codes2)