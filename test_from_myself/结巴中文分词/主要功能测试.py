
#jeiba : https://github.com/fxsjy/jieba
import jieba

words="我来到北京清华大学念书"

# 全模式
myList=jieba.cut(words,cut_all=True)
print("Full Mode : ","/".join(myList))
# Full Mode :  我/来到/北京/清华/清华大学/华大/大学/念书

#精确模式
myList=jieba.cut(words,cut_all=False)
print("Default Mode : ","/".join(myList))
# Default Mode :  我/来到/北京/清华大学/念书 

#默认精确模式
myList=jieba.cut("我来到了杭州研杭大厦")
print("【新词识别】","/".join(myList))
# 【新词识别】 我/来到/了/杭州/研杭/大厦

# 搜索引擎模式
myList=jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print("【搜索引擎模式】","/".join(myList))
# 【搜索引擎模式】 小明/硕士/毕业/于/中国/科学/学院/科学院/中国科学院/计算/计算所/，
# /后/在/日本/京都/大学/日本京都大学/深造

