# 8. Composite（组合）
# 将对象组合成树形结构以表示“部分-整体”的层次结构。
# Composite 使得用户对单个对象和组合对象的使用具有一致性。 

class Component(object):
    def __init__(self, name):
        self.name = name

    def add(self, com):
        pass

    def display(self, depth):
        pass


class Leaf(Component):
    def add(self, com):
        print("leaf can't add")

    def display(self, depth):
        temp = "-"*depth
        temp = temp + self.name
        print(temp)

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.c = []

    def add(self, com):
        self.c.append(com)

    def display(self, depth):
        temp = "-"*depth
        temp = temp + self.name
        print(temp)
        for com in self.c:
            com.display(depth+2)

if __name__ == '__main__':
    p=Composite("li")
    p.add(Leaf("Lee"))
    p.add(Leaf("Zhao"))

    p1= Composite("Wu")
    p1.add(Leaf("San"))
    p.add(p1)

    p.display(1)

    """
    -li
    ---Lee
    ---Zhao
    ---Wu
    -----San
    """