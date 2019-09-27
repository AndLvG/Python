class AmericanDate:

    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def get_year(self):
        return str(self.y)

    def get_month(self):
        return str(self.m).rjust(2, '0')

    def get_day(self):
        return str(self.d).rjust(2, '0')

    def set_year(self, ny):
        self.y = ny
        return self.y

    def set_month(self, nm):
        self.m = str(nm)
        return str(self.m)

    def set_day(self, nd):
        self.d = str(nd)
        return self.d

    def format(self):
        return f'{self.get_month()}.{self.get_day()}.{self.get_year()}'


class EuropeanDate:

    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def get_year(self):
        return str(self.y)

    def get_month(self):
        return str(self.m).rjust(2, '0')

    def get_day(self):
        return str(self.d).rjust(2, '0')

    def set_year(self, ny):
        self.y = ny
        return self.y

    def set_month(self, nm):
        self.m = str(nm)
        return str(self.m)

    def set_day(self, nd):
        self.d = str(nd)
        return self.d

    def format(self):
        return f'{self.get_day()}.{self.get_month()}.{self.get_year()}'


# american = AmericanDate(2000, 4, 10)
# european = EuropeanDate(2000, 4, 10)
# print(american.format())
# print(european.format())
