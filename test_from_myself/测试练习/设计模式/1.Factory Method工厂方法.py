# １．Factory Method（工厂方法）
# 定义一个用于创建对象的接口，让子类决定实例化哪一个类


class Chinese(object):
    def say_hello(self):
        print("你好！")


class English(object):
    def say_hello(self):
        print("Hello!")


def get_man(language="chinese"):
    """The factory method"""
    languages = dict(chinese = Chinese, english = English)
    return languages[language]()


chinese = get_man("chinese")
chinese.say_hello()  # 你好！

english = get_man("english")
english.say_hello()  # Hello!
