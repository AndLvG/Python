def Eratosthenes(n):
    a = [n for n in range(n + 1)]
    a[0] = 0
    a[1] = 0
    for i in range(2, len(a)):
        if a[i] > 0:
            for j in range(i * i, n + 1, i):
                if a[j] > 0:
                    print(a[j], end=" ")
                    a[j] = 0
    print()
    return [x for x in a if x > 0]


print(Eratosthenes(15))
