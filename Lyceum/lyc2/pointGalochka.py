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
        if self.x != other.x:
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


class CheckMark():
    def __init__(self, A_point, B_point, C_point):
        self.A_point = A_point
        self.B_point = B_point
        self.C_point = C_point

    def __str__(self):
        return f"{self.A_point.name}{self.B_point.name}{self.C_point.name}"

    def __bool__(self):
        return not (self.C_point.x * (self.B_point.y - self.A_point.y) - self.C_point.y * (
                self.B_point.x - self.A_point.x) ==
                    self.A_point.x * self.B_point.y - self.B_point.x * self.A_point.y)
        # if self.B_point.x - self.A_point.x != 0:
        #     a1 = (self.C_point.x - self.A_point.x) / (self.B_point.x - self.A_point.x)
        # else:
        #     a1 = 0
        # if self.B_point.y - self.A_point.y != 0:
        #     a2 = (self.C_point.y - self.A_point.y) / (self.B_point.y - self.A_point.y)
        # else:
        #     a2 = 0
        # if a1 == a2:
        #     return False
        # else:
        #     return True

    def __eq__(self, other):
        if self.B_point == other.B_point and ((self.A_point == other.A_point and self.C_point == other.C_point) or
                                              (self.A_point == other.C_point and self.C_point == other.A_point)):
            return True
        else:
            return False


# p_A = Point('A', 1, 2)
# p_B = Point('B', 0, 1)
# p_C = Point('C', -1, 2)
# p_D = Point('D', 2, 2)
# p_E = Point('E', 2, 0)
# p_F = Point('F', 2, -1)
# cm_ABC = CheckMark(p_A, p_B, p_C)
# cm_DEF = CheckMark(p_D, p_E, p_F)
# cm_ABB = CheckMark(p_A, p_B, p_B)
# print(cm_ABC, bool(cm_ABC))
# print(cm_DEF, bool(cm_DEF))
# print(cm_ABB, bool(cm_ABB))
