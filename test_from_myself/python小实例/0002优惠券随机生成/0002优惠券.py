#第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，
#为你的应用**生成激活码**（或者优惠券），
#使用 Python 如何生成 200 个激活码（或者优惠券）

import random, string

forSelect = string.ascii_letters + "0123456789"

# 《Python编程：字符串处理》
# http://blog.sina.com.cn/s/blog_989218ad0102ww80.html

print(forSelect)
def generate(count, length):
    # count = 200
    # length = 20

    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)

if __name__ == "__main__":
    generate(200, 20)
    #随机数
    
    print(random.random())#1、随机浮点数[0,1)]
    print(random.uniform(0,10))#1、随机浮点数

    print(random.randint(0,10))#随机整数n: 0 <= n <= 10
    print(random.randrange(0,101,2))#随机选取0到100间的偶数
    print(random.choice('abc'))#随机字符
    print(random.sample('abcadfasdfas',3))#多个字符中选取特定数量的字符
    item=['1','2','3','4']
    random.shuffle(item)#洗牌
    print(item)
    #print(string.join(random.sample(['a','b','c','d','e','f','g','h'],3)).replace(" ",""))