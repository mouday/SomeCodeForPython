# 7. Bridge（桥接）
# 将抽象部分与它的实现部分分离，使它们都可以独立地变化


class DrawingAPI1(object):
    def draw_circle(self, x, y, radius):
        print("API1.circle as {}:{} radius {}".format(x, y, radius))


class DrawingAPI2(object):
    def draw_circle(self, x, y, radius):
        print("API2.circle as {}:{} radius {}".format(x, y, radius))

class CircleShape(object):
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, pct):
        self._radius *= pct

def main():
    shapes = (
        CircleShape(1, 3, 5, DrawingAPI1()),
        CircleShape(2, 4, 6, DrawingAPI2())
        )

    for shape in shapes:
        shape.scale(2)
        shape.draw()


if __name__ == '__main__':
    main()