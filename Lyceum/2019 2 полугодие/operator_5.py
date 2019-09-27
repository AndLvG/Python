class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum([self.coefficients[i] * x ** i for i in range(len(self.coefficients))])

    def __add__(self, p):
        a = self.coefficients
        b = p.coefficients
        if len(a) < len(b):
            a += [0] * (len(b) - len(a))
        else:
            b += [0] * (len(a) - len(b))
        return Polynomial([a[i] + b[i] for i in range(len(a))])


# poly1 = Polynomial([0, 0, 1])
# print(poly1(-2))
# print(poly1(-1))
# print(poly1(0))
# print(poly1(1))
# print(poly1(2))
# print()
#
# poly2 = Polynomial([0, 0, 2])
# print(poly2(-2))
# print(poly2(-1))
# print(poly2(0))
# print(poly2(1))
# print(poly2(2))
# print()
#
# poly3 = poly1 + poly2
# print(poly3(-2))
# print(poly3(-1))
# print(poly3(0))
# print(poly3(1))
# print(poly3(2))
# print()
