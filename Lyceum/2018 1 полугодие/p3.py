a = [1]
for i in range(int(input())):
    print(*a)
    b = [1]
    b += [a[k] + a[k + 1] for k in range(len(a) - 1)] + [1]
    a = b
