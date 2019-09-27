sp = {}
n = int(input())
for i in range(n):
    name = input().split()
    if name[2] in sp:
        sp[name[2]].append(name[0])
    else:
        sp[name[2]] = [name[0]]
num = int(input())
for i in range(num):
    arr = []
    word = input()
    if word in sp:
        arr = sorted(sp[word])
        print(' '.join(arr))
    if word not in sp:
        print()
