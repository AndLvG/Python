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


# Bell("бронзовый").print_info()
# LittleBell("медный", нота="ля").print_info()
# BigBell(название="Корноухий", вес="1275 пудов").print_info()

# bells = [BigBell("крупнейший в мире действующий колокол",
#                  название="Bell of Good Luck", высота="810,8 см",
#                  диаметр="511,8 см", вес="116 тонн"),
#          Bell("четвёртый по счёту",
#               "отлит по приказу императрицы Анны Иоановны",
#               "ни разу не звонил", название="Царь-колокол",
#               создан="25 ноября 1735 года", ),
#          BigBell("появился при храме в 1633 году",
#                  "в Новый год выполняет функцию курантов, отсчитывая 108 ударов",
#                  название="Большой колокол храма Тион-ин", диаметр="2,8 м",
#                  высота="3,3 м", вес="74 тонны")
#          ]
# for bell in bells:
#     bell.print_info()
