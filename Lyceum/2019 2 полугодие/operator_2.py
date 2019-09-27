from datetime import datetime


class Date:
    def __init__(self, m, d):
        self.m = m
        self.d = d

    def __sub__(self, d2):
        d1 = datetime.strptime("2019-{}-{}".format(str(self.m), str(self.d)), "%Y-%m-%d")
        d2 = datetime.strptime("2019-{}-{}".format(str(d2.m), str(d2.d)), "%Y-%m-%d")

        return (d1 - d2).days


mar5 = Date(3, 1)
jan1 = Date(1, 1)

print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)
