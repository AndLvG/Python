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

    def __eq__(self, other):
        if self.name != other.name:
            return self.name == other.name
        elif self.x != other.x:
            return self.x == other.x
        elif self.y != other.y:
            return self.y == other.y
        else:
            return True

    def __ne__(self, other):
        if self.name != other.name:
            return self.name != other.name
        elif self.x != other.x:
            return self.x != other.x
        elif self.y != other.y:
            return self.y != other.y
        else:
            return False

    def __gt__(self, other):
        if self.name != other.name:
            return self.name > other.name
        elif self.x != other.x:
            return self.x > other.x
        elif self.y != other.y:
            return self.y > other.y
        else:
            return False

    def __lt__(self, other):
        if self.name != other.name:
            return self.name < other.name
        elif self.x != other.x:
            return self.x < other.x
        elif self.y != other.y:
            return self.y < other.y
        else:
            return False

    def __ge__(self, other):
        if self.name != other.name:
            return self.name >= other.name
        elif self.x != other.x:
            return self.x >= other.x
        elif self.y != other.y:
            return self.y >= other.y
        else:
            return True

    def __le__(self, other):
        if self.name != other.name:
            return self.name <= other.name
        elif self.x != other.x:
            return self.x <= other.x
        elif self.y != other.y:
            return self.y <= other.y
        else:
            return True

    def __hash__(self):
        return 0


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


# p_A1 = Point('A', 1, 2)
# p_A2 = Point('A', 2, 1)
# p_B1 = Point('B', 2, 3)
# p_B2 = Point('B', 2, 3)
# # print(p_A1 == p_A2, p_B1 == p_B2)
# # print(p_A1 != p_A2, p_B1 != p_B2)
# # print(p_A1 < p_A2, p_B1 > p_B2)
# print(p_A1 >= p_A2, p_B1 <= p_B2)
# # print(max(p_A1, p_B2, p_A2, p_B2))
# # print(min(p_A1, p_B2, p_A2, p_B2))
#
# # points = [Point('A', 101, 1), Point('B', -1, 0),
# #           Point('A', 11, 0), Point('A', 111, -11)]
# # points.sort()
# # print(', '.join(map(str, points)))
#
# # points = [Point("A", 0, 3), Point("A", 0, 3),
# #           Point("A", 3, 0), Point("A", 3, 0),
# #           Point("B", 0, 3), Point("A", 0, 3)]
# # points_dir = {}
# # for i, point in enumerate(points):
# #     points_dir[point] = i
# # print(["{}: {}".format(k, v) for k, v in sorted(points_dir.items())])
