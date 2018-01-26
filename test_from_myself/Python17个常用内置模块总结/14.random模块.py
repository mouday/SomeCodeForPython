import random

print(random.random())   # 0.2804757095959982
print(random.randint(1,2))  # 1
print(random.randrange(1,10)) # 2

# 随机验证码实例：
checkcode=""
for i in range(4):
    current=random.randrange(0,4)
    if current !=i:
        temp=chr(random.randint(65,90))
    else:
        temp=random.randint(0,9)
    checkcode+=str(temp)
print(checkcode)
# X28I