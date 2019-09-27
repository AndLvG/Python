def roots_of_quadratic_equation(*k):
    a, b, c = k[0], k[1], k[2]
    D = b ** 2 - 4 * a * c
    if D >= 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2
    else:
        return []


def solve(*coeffs):
    if len(coeffs) == 3:
        return set(roots_of_quadratic_equation(*coeffs))
    elif len(coeffs) == 2:
        b, c = coeffs[0], coeffs[1]
        return [-c / b]
    elif len(coeffs) == 1:
        if coeffs[0] == 0:
            return ['all']
        else:
            return []
    else:
        return['None']


#  print(sorted(solve(1, 2, 3)))
#  print(sorted(solve(1, 2, 1)))
str = map(int, input().split())
#  s = map(int, '1 2 1'.split())
print(*solve(*str))
