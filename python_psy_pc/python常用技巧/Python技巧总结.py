# Python 技巧总结
# http://litaotao.github.io/python-materials

def enumerate_test():
    # 1. 枚举 - enumerate 可以有参数
    for index, value in enumerate(range(10)):
        print(index,"->",value)

    print(list(enumerate("abc")))

    # 接收第二个参数,指明索引的起始值
    print(list(enumerate("abc",1)))


def dict_test():
    # 2. 字典/集合 解析
    print({i: i*i for i in range(10)})
    print([i for i in range(10)])
    # 两者的区别在于字典推导中有冒号

def division_test():
    # 3. 浮点除法
    print(5/2) # 浮点除法
    print(5//2) # 整除

def eval_test():
    # 4. 对Python表达式求值
    s="[1,2,3,4,5]"
    print(type(s),s)
    print(type(eval(s)),eval(s))

def str_reverse():
    # 5. 字符串/数列 逆序
    a=[1,2,3,4,5]
    print(a,"\n",a[::-1])
    print(a.reverse())

    b="abcdef"
    print(b,"\n",b[::-1])

def if_else_test():
    # 6. 三元运算
    a=True if 1 else False
    print(a)

def copy_test():
    # 7. Python里面拷贝一个对象
    lst=[1,2,3,[4,5]]
    print("lst",lst)
    
    import copy
    # 浅拷贝
    lst2=copy.copy(lst)
    print("lst2",lst2)

    lst.append(6)
    print("lst",lst)
    print("lst2",lst2)
    
    lst[3].append(7)
    print("lst",lst)
    print("lst2",lst2)

    # 深拷贝
    lst3=copy.deepcopy(lst)
    print("lst3",lst3)

    lst.append(8)
    print("lst",lst)
    print("lst3",lst3)
    
    lst[3].append(9)
    print("lst",lst)
    print("lst3",lst3)

def equal_test():
    """
    8、python中的 ==
    python中的对象包含三要素:id, type, value
    id 用来标识唯一一个对象，type标识对象的类型，value用来设置对象的值。
    is 判断是否是一个对象，使用id来判断的。
    == 是判断a对象的值是否是b对象的值，默认调用它的__eq__方法。
    """
    a=1
    b=1
    print(a==b)
    print(a is b)

    c="abc"
    d="abc"
    print(a==b)
    print(a is b)

def compare_test():
    # 9.链式比较操作符,级联比较
    x=4
    print(1 < x <5)

def default_arg():
    # 10.函数的默认参数
    def foo(lst=[]):
        lst.append(1)
        print(lst)

    foo()
    foo()

    # 更安全的做法是
    def func(lst=None):
        if lst ==None:
            lst=[]
        lst.append(1)
        print(lst)

    func()
    func()

def format_test():
    # 11.带关键字的格式化
    print("my name is %(name)s"%{"name":"Tom"})
    print("Tom is %(age)i yeas old "% {"age": 23})
    print("Tom sex is {sex}".format(sex="man"))

def slice_test():
    # 12.切片操作的步长参数
    a=[1,2,3,4,5,6,7,8]
    print(a[::2])
    print(a[::-1])# 反转

def list_test():
    # 13.嵌套列表推导式
    print([(i,j) for i in range(10) for j in range(i)])
    a="abcd"
    print([i+j+k for i in a for j in a.replace(i,"") for k in a.replace(i,"").replace(j,"")])

def tuple_test():
    # 14.元组unpack
    lst=[x for x in range(10)]
    print(lst)
    a, b, *c = lst
    print("lst",lst)
    print("a",a)
    print("b",b)
    print("c",c)

    a, *b, c = lst
    print("lst",lst)
    print("a",a)
    print("b",b)
    print("c",c)

def pow_test():
    # 15.pow的第三个参数
    # 其实第三个参数是来求模的: pow(x, y, z) == (x ** y) % z，
    # 注意，内置的 pow 和 math.pow 并不是一个函数，后者只接受2个参数。
    print(pow(2, 3, 3))
    print(2 ** 3 % 3)

def set_test():
    # 16.声明一个集合
    s={1,2,3}
    print(type(s),s)

def del_test():
    # 17.用切片来删除序列的某一段
    a=[1,2,3,4,5,6,7,8,9]
    print(a)
    a[1:4]=[]
    print(a)
    # 去除偶数项(偶数索引的)
    del a[::2]
    print(a)

def isinstance_test():
    # 18.isinstance可以接收一个元组，元组里面是 或 的关系
    print(isinstance(1, (float, int)))
    print(isinstance(1.1, (float, int)))
    print(isinstance("1.1", (float, int)))

def sort_test():
    # 19.排序时使用键（key）
    import operator 
    lst=[(1,2,3),(2,1,3),(3,2,1)]
    lst.sort()
    print(lst)
    lst.sort(key=operator.itemgetter(1))
    print(lst)
    lst.sort(key=operator.itemgetter(2))
    print(lst)

def generator_test():
    # 20.生成器(Generator)
    # 生成器表达式同列表推导式有着几乎相同的语法结构，
    # 区别在于生成器表达式是被圆括号包围，而不是方括号：
    nums=[1, 4, -5, 10, -7, 2, 3, -1]
    lst=(x for x in nums if x>0)
    print(lst)
    for x in lst:
        print(x,end=" ")

def walk_test():
    def tree():
        import os
        """
        21.os.walk()返回的是一个三元tupple(dirpath, dirnames, filenames)
        dirpath是一个string，代表起始目录的路径,
        dirnames是一个list，包含了dirpath下所有子目录的名字,
        filenames是一个list，包含了非目录文件的名字.这些名字不包含路径信息,
        如果需要得到全路径,需要使用 os.path.join(dirpath, name).
        """
        p="D:\\迅雷下载"
        for path,names,fnames in os.walk(p):
            for fname in fnames:
                # 生成器表达式
                yield os.path.join(path,fname)

    for x in tree():
        print(x)

def decorator_test():
    # 22.装饰器(Decorator)
    def print_log(func):
        print("start")
        return func
    
    @print_log
    def main():
        print("main")

    main()

def contextLib_test():
    # 23.上下文管理库(ContextLib)
    import time 
    class demo:
        def __init__(self,label):
            self.label=label

        def __enter__(self):
            # 当执行流进入with代码块时
            self.start=time.time()

        def __exit__(self, exc_ty, exc_val, exc_tb):
            # 执行流离开with代码块时
            end=time.time()
            print("{}:{}".format(self.label, end- self.start))

    from contextlib import contextmanager
    @contextmanager
    def demo1(label):
        #函数中yield之前的所有代码都类似于上下文管理器中__enter__方法的内容。
        #而yield之后的所有代码都如__exit__方法的内容。
        #如果执行过程中发生了异常，则会在yield语句触发。
        start =time.time()
        try:
            yield
        finally:
            end = time.time()
            print("{}:{}".format(label,end-start))
    
    with demo1("counting"):
        n=10000000
        while n>0:
            n-=1

def descriptor_test():
    """
    24.描述器(Descriptors)
    描述器决定了对象属性是如何被访问的。
    描述器的作用是定制当你想引用一个属性时所发生的操作。
    构建描述器的方法是至少定义以下三个方法中的一个。
    需要注意，下文中的instance是包含被访问属性的对象实例，
    而owner则是被描述器修辞的类。
    get(self, instance, owner) – 这个方法是当属性被通过(value = obj.attr)的方式获取时调用，
    这个方法的返回值将被赋给请求此属性值的代码部分。 
    set(self, instance, value) – 这个方法是当希望设置属性的值(obj.attr = ‘value’)时被调用，
    该方法不会返回任何值。 
    delete(self, instance) – 当从一个对象中删除一个属性时(del obj.attr)，调用此方法。 
    译者注：对于instance和owner的理解，考虑以下代码：
    """
    class Celsius(object):
        def __init__(self, value=0.0):
            print("init")
            self.value = float(value)

        def __get__(self, instance, owner):
            print("get")
            return self.value

        def __set__(self, instance, value):
            print("set")
            self.value = flaot(value)

        def __delete__(self, instance):
            print("delete")

    class Temperature(object):
        celsius = Celsius()

    temp=Temperature()
    temp.celsius

def zip_test():
    # 25.zip test
    a=[1,2,3,4,5,6]
    b=["a", "b", "c", "d", "e"]
    z=zip(a,b)
    print(z,list(z))

def grouping_adjacent_test():
    a=[1, 2, 3, 4, 5, 6]
    # using iterators
    group_adjacent = lambda a, k: zip(*([iter(a)]*k))
    print(list(group_adjacent(a,3)))
    print(list(group_adjacent(a,2)))
    print(list(group_adjacent(a,1)))

def star_test():
    a=[1,2,3,4]
    print(a)
    print(*a)

def inverting_dictionary():
    a={"a": 1, "b": 2, "c": 3, "d": 4}
    b=dict(zip(a.values(),a.keys()))
    print(b)

def flattening_list():
    a=[[1,2,3],[4,5,6],[7,8,9,[10,11,12]]]
    print(sum(a,[]))

# Python的作用域解析是基于LEGB规则，
# 分别是Local、Enclosing、Global、Built-in

def odd_test():
    #奇数
    odd=lambda x: bool(x % 2)
    numbers = [n for n in range(10)]
    numbers[:]=[n for n in numbers if not odd(n)]
    print(numbers)


# eval, cPickle, json方式三种对相应字符串反序列化
# 
# 内置函数：
# map，reduce，filter，iter，range，divmod，round，chr，enumerate，all，any，slice，zip+
# 
# 启动服务器：python -m http.server
if __name__ == '__main__':
    odd_test()