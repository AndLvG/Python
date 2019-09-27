n = int(input())
r = [[]]
for i in range(n - 1):
    s = input()
    r += [s.split()]
for i in range(n):
    row = ''
    for j in range(n):
        if i == j:
            row += '0 '
        elif j < i:
            row += r[i][j] + ' '
        else:
            row += r[j][i] + ' '
    print(row)
