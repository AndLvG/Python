n = int(input())
n1 = int(input())
m = []
c = []

for i in range(n):
    m1 = []
    for i1 in range(n1):
        a = input()
        c.append(a)
        m1.append(a)
    m.append(m1)

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end="\t")
    print()

for i in range(n1):
    for j in range(n):
        print(m[j][i], end="\t")
    print()

m = []
c1 = 0
print("")
for i in range(n1):
    m1 = []
    for i1 in range(n):
        m1.append(c[c1])
        c1 += 1
    m.append(m1)
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end="\t")
    print()