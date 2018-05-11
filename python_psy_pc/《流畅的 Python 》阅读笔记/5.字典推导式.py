# 散列表也叫哈希表, 对于dict类型, 它的key必须是可哈希的数据类型.
#  str, bytes, frozenset 和 数值 都是可散列类型.

DIAL_CODE=[
    (86,"China"),
    (91,"India"),
    (7,"Russia"),
    (81,"Japan")
]

# 利用字典推导快速生成字典
country_code={country:code for code,country in DIAL_CODE}

print(country_code)