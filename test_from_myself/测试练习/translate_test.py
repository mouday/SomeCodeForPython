# 测试translate函数

string = "1234"

# 方式一：通过字符串构建转换表
#原始字符表，转换字符表，删除字符表
table = str.maketrans("123", "ABC", "4")

ret = string.translate(table)

print(ret)  # ABC

# 方式二：通过字典构建转换表
dct = {
    "1": "AA",
    "2": "BB",
    "3": "CC"
}

# string keys in translate table must be of length 1
table = str.maketrans(dct)

ret = string.translate(table)

print(ret)  # AABBCC4