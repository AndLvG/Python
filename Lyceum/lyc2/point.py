class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.cords = (name, self.x, self.y)

    def __invert__(self):
        inv = (self.y, self.x)
        return Point(self.name, self.y, self.x)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return f"{self.cords[0]}({self.cords[1]}, {self.cords[2]})"


point_A = Point('A', 3, -4)
print(point_A)
point_B = ~point_A
print(point_B)
print(~Point('O', 0, 0))
