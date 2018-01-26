import datetime

print(dir(datetime))
print(dir(datetime.datetime))
print(datetime.time())
print(datetime.date(year=2015,month=12,day=11))
print(datetime.datetime.now())
print(datetime.datetime.now()-datetime.timedelta(days=5))

'''
datetime.date：表示日期的类。常用的属性有year, month, day
datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond
datetime.datetime：表示日期时间
datetime.timedelta：表示时间间隔，即两个时间点之间的长度
timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
strftime("%Y-%m-%d")
'''