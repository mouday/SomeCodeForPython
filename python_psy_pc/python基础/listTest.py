#定义list
#     0,     1,    2,    3
l=["farther",20,"mother",20]
#变量“l”存储了list的地址，也就是引用
print(type(l))
print(dir(l))
print(l)

#增加
l.append("jack")
l.insert(1,"test")
print(l)
l+=["tom",90]
print(l)
#删除
l.remove("jack")
print(l)
del(l[0])
print(l)
#查询
print(l[0])
print(l[-1])

#修改
l[1]=30
print(l)

#list切片
print(l[1:3])
print(l[1:])
print(l[:2])

#拷贝,=仅仅拷贝了首地址
l2=l
print(l2)
print(l)
l2[0]="jimi"
print(l2)
print(l)

l3=list(l)
print(l3)
print(l)
l3[0]="dodo"
print(l3)
print(l)

l4=l[:]
print(l4)
print(l)
l4[0]="mimi"
print(l4)
print(l)

l5=[1,3,4,7,8,9,2,6,5,1,2,1]
print(max(l5))#获取最大值
print(min(l5))#获取最小值
print(len(l5))#获取长度
print(l5.count(1))#获取数量
print(l5.index(8))#获取索引
print(l5.sort())
print(l5.reverse())

print(round(1.86,1))
print(round(1.86))
print(round(1.49))
print(round(1.50))
print(round(1.51))
print(help(round))


