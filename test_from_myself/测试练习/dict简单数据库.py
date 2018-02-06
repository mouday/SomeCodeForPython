#dict简单数据库.py
#使用人名作为字典的键，每个人又用另一个字典表示
people={
	"Alice":{
		"phone":"2341",
		"addr":"foot drive 23"
	},
	"Beth":{
		"phone":"9012",
		"addr":"bar street 42"
	},
	"Cecil":{
		"phone":"3154",
		"addr":"Baz avenue 90"
	}
}
#描述性标签
labels={
	"phone":"phone number",
	"addr":"address"
}
name=input("Name:")
request=input("查找带电话(p)还是地址(a)？")
if request[0]=="p": key="phone"
if request[0]=="a": key="addr"
if name in people:
	print("%s %s is %s"%(name,labels[key],people[name][key]))
