class Bell:
    def __init__(self, *args, **kwargs):
        self.args_positional = []
        for arg in args:
            self.args_positional.append(arg)
        self.args_named = {arg: kwargs[arg] for arg in sorted(kwargs)}

    def print_info(self):
        result = ''
        for arg in self.args_named.keys():
            result += f'{arg}: {self.args_named[arg]}, '
        if result != '':
            result = result[0:-2]
        for arg in self.args_positional:
            if len(self.args_named) > 0:
                result += '; '
            result += arg

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


BigBell("крупнейший в мире действующий колокол", название="Bell of Good Luck",
        высота="810,8 см", диаметр="511,8 см", вес="116 тонн").print_info()
LittleBell().print_info()