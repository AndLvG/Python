x = int(input())
d = []
for i in range(x):
    d.append(input())
k = int(input())
n = 0
print(d[0])
del d[0]
for i in range(x):
    if len(d) > n + k - 1:
        n += k - 1
        print(d[n])
        del d[n]
    else:
        n = 0
        if len(d) > n:
            print(d[n])
            del d[n]