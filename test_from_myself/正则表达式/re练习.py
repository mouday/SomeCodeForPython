# 正则表达式

import re

# 查找字符
pattern = re.compile("a")  # 编译
match = pattern.findall("afdfdadfssdfadfdsadfd")
print(match)  # ['a', 'a', 'a', 'a']

# 查找数字
pattern = re.compile("\d+")
match = pattern.findall("asdf123fasdf23232dfsdf234fvdf2")
print(match)  # ['123', '23232', '234', '2']

# 查找单词
string = "1oo1 tina is a good girl ,she is cool"
pattern = re.compile("[a-zA-Z]oo[a-zA-Z]")

# 查找所有匹配
match = pattern.findall(string)
print(match)  # ['good', 'cool']

# 查找一个匹配
match = pattern.search(string)
print(match)  # <_sre.SRE_Match object; span=(15, 19), match='good'>

# 从开始匹配
match = pattern.match(string, 15)  # (string, pos, endpos)
print(match)  # <_sre.SRE_Match object; span=(15, 19), match='good'>

# 分割字符串
string = "i123am2234a44student"
pattern = re.compile("\d+")
match = pattern.split(string)  # (string, maxsplit)可指定最大分割次数
print(match)  # ['i', 'am', 'a', 'student']

# 替换字符串
string = "i123am2234a44student"
pattern = re.compile("\d+")
match = pattern.sub("*", string)
print(match)  # i*am*a*student

# 练习
"""
1 已知字符串:
info = <a href="http://www.baidu.com">baidu</a>
用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"
"""
string = '<a href="http://www.baidu.com">baidu</a>'

# 匹配网址和文本
pattern = re.compile("\w*\.?baidu\.?\w*")
match = pattern.findall(string)  
print(match)  # ['www.baidu.com', 'baidu']

# 匹配标签文本
text = re.compile(">(\w*)<")
match = text.search(string)
print(match.group(1))  # baidu

# 2 字符串："one1two2three3four4" 用正则处理，输出 "1234"

string = "one1two2three3four4"
pattern = re.compile("\d")
match = pattern.findall(string)
print("".join(match))  # 1234


"""
3 已知字符串：
text = "JGood is a handsome boy, he is cool, clever, and so on..." 
查找所有包含'oo'的单词。
"""
text = "JGood is a handsome boy, he is cool, clever, and so on..." 
pattern = re.compile("\w*oo\w*")
match = pattern.findall(text)
print(match)  # ['JGood', 'cool']

