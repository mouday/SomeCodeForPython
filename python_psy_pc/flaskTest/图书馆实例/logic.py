"""逻辑处理
"""
def get_home():
    """获取图书馆主页资料，一般是读取数据库或者缓存系统
    """
    return "home page"

def get_books():
    """获取图书馆书籍列表，一般是读取缓存系统
    """
    return "books"

def get_book(book_id):
    """获取一本书的信息，一般是数据库，如果比较热门，读取缓存
    """
    return "book id is {}".format(book_id)

def get_students():
    """获取学生列表，数据库
    """
    return "students"

def get_student(student_id):
    """获取一个学生的信息，一般是读取数据库
    """
    return "student id is {}".format(student_id)