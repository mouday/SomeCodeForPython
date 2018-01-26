import time
#三种存在方式
print(dir(time))

#时间戳形式存在
print(time.time())  #-->1511350552.05741
print(time.mktime(time.localtime()))#把元组形式转化成时间戳形式  -->1511350552.0

#元组形式存在
print(time.gmtime())
#-->time.struct_time(tm_year=2017, tm_mon=11, tm_mday=22, tm_hour=11, tm_min=35, tm_sec=52, tm_wday=2, tm_yday=326, tm_isdst=0)
print(time.localtime())
#-->time.struct_time(tm_year=2017, tm_mon=11, tm_mday=22, tm_hour=19, tm_min=35, tm_sec=52, tm_wday=2, tm_yday=326, tm_isdst=0)
print(time.strptime("2017-12-12","%Y-%m-%d")) #字符串形式转换成元组形式
#-->time.struct_time(tm_year=2017, tm_mon=12, tm_mday=12, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=346, tm_isdst=-1)

#字符串形式存在
print(time.strftime("%Y-%m-%d")  #默认当前时间，必须记住，工作中用得最多  -->2017-11-22
print(time.strftime("%Y-%m-%d",time.localtime()))#默认当前时间  -->2017-11-22
print(time.asctime())           #-->Wed Nov 22 19:35:52 2017
print(time.ctime(time.time()))  #-->Wed Nov 22 19:35:52 2017