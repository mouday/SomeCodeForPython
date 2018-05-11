import pandas as pd
#基于numpy
csv=pd.read_csv("bricks.csv",index_col=0)
print(csv)
print(csv.nation)#获取列
print(csv["nation"])
csv["note"]=[1,2,3,4,5,6,7,8,9]#新加列
print(csv)
csv["densty"]=csv["area"]/csv['peple']
print(csv)
print(csv.loc["ch"])#获取行数据
print(csv["nation"].loc["ch"])#获取元素
print(csv.loc["ch"]["nation"])
print(csv.loc["ch","nation"])

