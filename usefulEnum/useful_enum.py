from enum import Enum, unique

@unique
class Weekday(Enum):
    """星期"""
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

@unique
class Gender(Enum):
    """性别"""
    Male = 0
    Famale = 1

# 月份枚举
Month = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))