import re

'''
compile
match search findall
group groups
正则表达式常用格式：
　　字符：\d \w \t
　　次数：* + ? {m} {m,n}
'''
print(dir(re))

result=re.match("\d+","123sdfasdf123456")#在你给的字符串起始位置去匹配,\d从数字开始找，+表示一个到多个
if result:  #当result等于True的时候，就是匹配
    print(result.group())  #用group方法把他匹配的内容输出出来
else:
    print("nothing")

result=re.search("\d+","asdfa1223")#在整个内容里面去匹配，\d从数字开始找，+表示一个到多个
if result:
    print(result.group())

result=re.findall("\d+","123adfa134afd32r43") #只要匹配全都拿出来
print(result)

patern=re.compile("\d+")
result=patern.findall("asdf1234zsdf32423")
print(result)

result=re.search("(\d+)\w*(\d+)","aasflsjfa12aaljsf22lj13bb")
print(result.group()) #所有匹配内容输出  --》12aaljsf22lj13
print(result.groups())#只把括号\d，也就是组里面的内容输出  --》('12', '3')

result=re.search("a{3,5}","aaaaaaaaa")  #匹配3到5次的aaaaa输出出来
print(result.group())

'''
总结：
match：只在第一个字符串开始找，如果没有匹配，则不再继续找，如果第一个字符串中有，则只输出第一个
searh: 在所有内容里找，直到找到为止，但只输出找到的第一个
findall：把所有找到的匹配的内容，都通过列表的形式打印出来
compile: 编译之后再去匹配，这样可以加快匹配的速度
group: 把他匹配的内容输出出来
groups：分组

匹配的字符：
\d：表示数字的意思
\w: 代表下划线，字母，数字
\t：制表符，除了回车以外的所有字符

匹配的次数：
* 大于等于0，0到多个
+ 大于等于1，1个到多个
?  0或1
{m} 次数，如a{6}，出现6次a的进行匹配
{m,n} 如a{3,7} 出现3到7次的就进行匹配
'''