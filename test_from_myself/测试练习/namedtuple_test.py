# 具名元组

from collections import namedtuple

student = namedtuple("student", ["name", "age", "grade"])

std = student("Tom", 23, 100)

print(type(std))
print(type(student))

print(std.name)
print(std.age)
print(std.grade)
"""
<class '__main__.student'>
<class 'type'>
Tom
23
100
"""