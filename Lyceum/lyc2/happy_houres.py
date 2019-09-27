h = sorted(list(map(int, input().split())))
m = sorted(list(map(int, input().split())))

print(h, m)

for e1 in h:
    for e2 in m:
        print(str(e1).rjust(2, '0') + ':' + str(e2).rjust(2, '0'))
