class ParentClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2


class ChildClass(ParentClass):
    def __init__(self, arg1, arg2, arg3):
        super().__init__(arg1, arg2)
        self.arg3 = arg3

c = ChildClass(1, 2, 3)
print(c.arg1)  # 1
print(c.arg2)  # 2
print(c.arg3)  # 3