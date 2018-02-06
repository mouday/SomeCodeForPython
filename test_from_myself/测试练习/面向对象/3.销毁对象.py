# 对象销毁 - 引用计数器和一个循环垃圾收集器
# 通常你需要在单独的文件中定义一个类
class Point(object):
    def __init__(self, x , y): # 构造函数
        self.x = x
        self.y = y

    def __del__(self):  # 析构函数 
        class_name = self.__class__.__name__
        print(class_name, "销毁")


p1 = Point(1, 4)
p2 = p1
p3 = p1
print(id(p1), id(p2), id(p3))  # 打印对象的id
# 18991312 18991312 18991312
del p1
del p2
del p3
# Point 销毁
print("="*50)

