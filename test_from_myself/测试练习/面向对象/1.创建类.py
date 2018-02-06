# 创建类
class Employee(object):
    """所有员工的基类"""
    empCount = 0  # 类变量

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: %s Salary: %d" % (self.name, self.salary))

# 创建 Employee 类的对象
employeeA = Employee("Tom", 2000)
employeeB = Employee("Jack", 2500)
employeeC = Employee("Jimi", 3000)

# 访问数据成员

# 访问类变量
print(Employee.empCount)  # 使用类名称访问类变量  3

# 访问实例变量
# 添加，删除，修改类的属性
employeeA.age = 23  # 添加
employeeA.age = 24  # 修改
del employeeA.age  # 删除

setattr(employeeB, "age", 25)  # 设置属性，不存在则新建
print(hasattr(employeeB, "age"))  # 检查属性存在  True
print(getattr(employeeB,"age"))  # 访问对象属性  25
delattr(employeeB, "age")  # 删除属性


# 访问对象方法
employeeA.displayCount()  # Total Employee 3
employeeA.displayEmployee()  # Name: Tom Salary: 2000 
employeeB.displayEmployee()  # Name: Jack Salary: 2500
employeeC.displayEmployee()  # Name: Jimi Salary: 3000

# 内置类属性
print(Employee.__doc__)  # 打印类文档  所有员工的基类
print(Employee.__name__)  # 类名  Employee
print(Employee.__module__)  # 类定义所在的模块  __main__
print(Employee.__base__)  # tuple 类的所有父类<class 'object'>
print(Employee.__dict__)  # dict 类的属性（由类的数据属性组成）
"""
{
    '__dict__': <attribute '__dict__' of 'Employee' objects>, 
    '__init__': <function Employee.__init__ at 0x0000000001263A60>, 
    '__weakref__': <attribute '__weakref__' of 'Employee' objects>,
    '__module__': '__main__', 
    '__doc__': '所有员工的基类', 
    'empCount': 3, 
    'displayCount': <function Employee.displayCount at 0x0000000001263AE8>, 
    'displayEmployee': <function Employee.displayEmployee at 0x0000000001263E18>
}
"""
