# 基础重载方法
class Student(object):
    def __init__(self, name, age):  # 构造函数
        self.name = name
        self.age = age

    def __del__(self):  # 析构方法, 删除一个对象del调用
        print("del")

    def __str__(self):  # 用于将值转化为适于人阅读的形式 str(obj)
        return "name:"+self.name+";age:"+str(self.age)

    __repr__ = __str__  # 转化为供解释器读取的形式

    def __cmp__(self,student):  #对象比较,用于排序   py3中删除
        if self.age > student.age:
            return 1
        elif self.age < student.age:
            return -1
        else:
            return 0

    def __add__(self, student):  # 运算符重载
        return Student(self.name,self.age+student.age)

student1 = Student("Tom", 23)
student2 = Student("Jack", 25)
student3 = Student("Jimi", 24)

print(repr(student1))  # name:Tom;age:23
print(str(student1))  # name:Tom;age:23
print(student1)  # name:Tom;age:23

print(student1+student2) # name:Tom;age:48