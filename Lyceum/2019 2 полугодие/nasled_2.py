class Summator:

    def __init__(self, num=1):
        self.num = num

    def transform(self, n, num):
        a = []
        for el in range(1, n + 1):
            a.append(el ** num)
        return a

    def sum(self, N):
        num = self.num
        a = Summator().transform(N, num)
        return sum(a)


class PowerSummator(Summator):
    def __init__(self, b):
        super().__init__(b)


class SquareSummator(PowerSummator):

    def __init__(self, num=2):
        super().__init__(num)


class CubeSummator(PowerSummator):

    def __init__(self, num=3):
        super().__init__(num)
