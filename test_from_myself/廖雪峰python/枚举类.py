
from enum import Enum, unique

# 方法一：
Month = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 默认从1开始计数
for name, member in Month.__members__.items():
    print(name, "=>", member, ":", member.value)

print(Month.Mar)
print(Month.Mar.name)
print(Month.Mar.value)


# 方法二：
@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Mon)
print(Weekday(1))
print(Weekday["Mon"])


# 实例
# 性别枚举
class Genger(Enum):
    Male = 0
    Famale = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


stu = Student("Tom", Genger.Male)

if stu.gender == Genger.Male:
    print("学生性别是男性")
else:
    print("学生性别不是男性")
