# 3. Builder（建造者）
# 将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示


class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


# abstract builder
class Builder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()


class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor = "One"

    def build_size(self):
        self.building.size = "Big"


class BuilderFlat(Builder):
    def build_floor(self):
        self.building.floor = "More than One"

    def build_size(self):
        self.building.size = "Small"


# product
class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return "Floor: %s | Size: %s " % (self.floor, self.size)


if __name__ == '__main__':
    director = Director()
    director.builder = BuilderHouse()
    director.construct_building()
    building = director.get_building()
    print(building)  # Floor: One | Size: Big 

    director.builder = BuilderFlat()
    director.construct_building()
    building = director.get_building()
    print(building)  # Floor: More than One | Size: Small 
