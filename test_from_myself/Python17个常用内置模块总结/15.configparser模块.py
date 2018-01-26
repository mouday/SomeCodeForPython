'''
用于对特定的配置进行操作，当前模块的名称在 python 3.x 版本中变更为 configparser。
1.读取配置文件
-read(filename) 直接读取ini文件内容
-sections() 得到所有的section，并以列表的形式返回
-options(section) 得到该section的所有option
-items(section) 得到该section的所有键值对
-get(section,option) 得到section中option的值，返回为string类型
-getint(section,option) 得到section中option的值，返回为int类型
 
2.写入配置文件
-add_section(section) 添加一个新的section
-set( section, option, value) 对section中的option进行设置
         需要调用write将内容写入配置文件。
'''

"""要读写的ini文件
[sec_a]
a_key1 = 20
a_key2 = 10
 
[sec_b]
b_key1 = 121
b_key2 = b_value2
b_key3 = $r
b_key4 = 127.0.0.1
"""

import configparser

#读取
cf=configparser.ConfigParser()
cf.read("data.ini")
print(cf)  
# <configparser.ConfigParser object at 0x00000000011F79E8>

secs=cf.sections()  # 获得所有区域
print("sections:",secs)
# sections: ['sec_a', 'sec_b']

opts=cf.options("sec_a")  # 获取区域的所有key
print(opts)
# ['a_key1', 'a_key2']

#打印出每个区域的所有属性
for sec in secs:
    print(cf.options(sec))
# ['a_key1', 'a_key2']
# ['b_key1', 'b_key2', 'b_key3', 'b_key4']

items = cf.items("sec_a")  # 获取键值对
print(items)
# [('a_key1', '20'), ('a_key2', '10')]

val=cf.get("sec_a","a_key1")
print(val)  # 20
print(type(val))  #--><class 'str'>

val=cf.getint("sec_a","a_key1")
print(val)  # 20
print(type(val))  #--><class 'int'>

#设置
cf.set("sec_b","b_key3","newvalue")
cf.add_section("newsection")
cf.set("newsection","new_key","new_value")

#写入
cf.write(open("data.txt","w"))

#判断
ret=cf.has_section("newsection") #判断存不存在
print(ret)  # True

cf.remove_section("newsection")#删除

ret=cf.has_section("newsection") #判断存不存在
print(ret)  # False

"""data.txt
[sec_a]
a_key1 = 20
a_key2 = 10

[sec_b]
b_key1 = 121
b_key2 = b_value2
b_key3 = newvalue
b_key4 = 127.0.0.1

[newsection]
new_key = new_value

"""