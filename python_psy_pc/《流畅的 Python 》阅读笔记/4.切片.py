s="bicycle"
print(s[::3])
print(s[::-1])
print(s[::-2])

# 列表中是以0作为第一个元素的下标, 切片可以根据下标提取某一个片段.
# 用 s[a:b:c] 的形式对 s 在 a 和 b 之间以 c 为间隔取值。
# c 的值还可以为负, 负值意味着反向取值.