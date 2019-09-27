n = int(input())

a = []

for i in range(n):
    n1 = int(input())
    a2 = [input().split() for i1 in range(n1)]
    a.append(a2)

otl = list()

for el in a:
    if any([e[1] == "5" for e in el]):
        otl.append(True)
    else:
        otl.append(False)
if all([el for el in otl]):
    print("ДА")
else:
    print("НЕТ")