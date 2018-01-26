#列表推导

symbols = "123456789"

#将字符串元素添加到列表
codes=[]

for symbol in symbols:
    codes.append(symbol)

print(codes)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#ord() unicode的码位
print("a:",ord("a"))  # a: 97

#列表推导
codes=[ord(symbol) for symbol in symbols]

print(codes)
# [49, 50, 51, 52, 53, 54, 55, 56, 57]
