class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x, self.y = x, y
        self.cords = (self.x, self.y)

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def get_coords(self):
        return self.cords

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"


class ColoredPoint(Point):
    def __init__(self, name, x, y, rgb=(0, 0, 0)):
        super(ColoredPoint, self).__init__(rgb, x, y)
        self.name = name
        self.rgb = rgb
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]

    def __invert__(self):
        return ColoredPoint(self.name, self.y, self.x,
                            (abs(self.r - 255), abs(self.g - 255), abs(self.b - 255)))

    def get_color(self):
        return self.rgb


# points = [Point('A', 0, 3), Point('B', 4, 0)]
# print(points)
# print(points[0])
# print(repr(points[0]))
