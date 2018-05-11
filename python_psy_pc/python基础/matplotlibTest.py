import matplotlib.pyplot as plt
year=[1950,1970,1999,2010]
pop=[2.519,3.692,5.263,6.972]
#加入历史数据
year=[1800,1850,1900]+year
pop=[1.0,1.262,1.650]+pop
#plt.plot(year,pop)#直线图
#plt.scatter(year,pop)#散点图
#plt.show()
plt.fill_between(year,pop,color="green")
values=[1,3,4,5,7,9,0,6,5,3,3,2,3,4,5,6,7,8,2]
#plt.hist(values,bins=3)#直方图
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("world population projections")
plt.yticks([0,2,4,6,8,10],
			["0B","2B","4B","6B","8B","10B"])#刻度
plt.show()