# from itertools import product


class Bell:
    def __init__(self, *args, **kwargs):
        self.args_positional = []
        for arg in args:
            self.args_positional.append(arg)
        self.args_named = {arg: kwargs[arg] for arg in sorted(kwargs)}

    def print_info(self):
        if len(self.args_positional) == 0 and len(self.args_named) == 0:
            print("-")
            return
        result = ''
        for arg in self.args_named.keys():
            result += f'{arg}: {self.args_named[arg]}, '
        if result != '':
            result = result[0:-2]
        if len(self.args_named) > 0:
            result += '; '
        for arg in self.args_positional:
            result += f'{arg}, '
        result = result[0:-2]

        print(result)


class LittleBell(Bell):
    def __init__(self, *args, **kwargs):
        super(LittleBell, self).__init__(*args, **kwargs)

    def sound(self):
        print("ding")


class BigBell(Bell):
    flag = False

    def __init__(self, *args, **kwargs):
        super(BigBell, self).__init__(*args, **kwargs)

    def sound(self):
        print('ding') if not self.flag else print('dong')
        self.flag = not self.flag


class BellTower:
    def __init__(self, *args):
        self.bells = []
        for arg in args:
            self.bells.append(arg)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')

    def print_info(self):
        n = 1

        for bell in self.bells:
            print(f'{n} {bell.__class__.__name__}')
            bell.print_info()
            n += 1
        print()


class SizedBellTower(BellTower):
    def __init__(self, *args, size=10):
        super(SizedBellTower, self).__init__(*args)
        self.size = size
        self.bells.clear()
        for arg in args:
            if len(self.bells) >= size:
                self.bells.pop(0)
            self.bells.append(arg)

    def append(self, bell):
        if len(self.bells) >= self.size:
            self.bells.pop(0)
        self.bells.append(bell)


class TypedBellTower(BellTower):
    def __init__(self, *args, bell_type=LittleBell):
        super(TypedBellTower, self).__init__(*args)
        self.bell_type = bell_type
        self.bells.clear()
        for arg in args:
            if arg.__class__.__name__ == bell_type.__name__:
                self.bells.append(arg)

    def append(self, bell):
        if bell.__class__.__name__ == self.bell_type.__name__:
            self.bells.append(bell)

# b_bt = TypedBellTower(BigBell("бронзовый"),
#                       LittleBell("медный", нота="ля"),
#                       BigBell(название="Корноухий", вес="1275 пудов"),
#                       bell_type=BigBell)
# l_bt = TypedBellTower(BigBell("бронзовый"),
#                       LittleBell("медный", нота="ля"),
#                       BigBell(название="Корноухий", вес="1275 пудов"))
# b_bt.print_info()
# l_bt.print_info()
#
# bb = BigBell("самый звонкий")
# lb = LittleBell("самый маленький")
# for bt, bell in product((b_bt, l_bt), (bb, lb)):
#     bt.append(bell)
#
# b_bt.print_info()
# l_bt.print_info()
