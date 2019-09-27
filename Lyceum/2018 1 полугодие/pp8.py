diction = {}
names = [input() for i in range(int(input()))]
for i in range(int(input())):
    name = input()
    for k in range(len(names)):
        if names[k] in name and name.find(names[k]) == 0:
            diction[name] = 'YES'
        else:
            diction[name] = 'NO'
            continue
        if diction[name] == 'YES':
            break
    print(diction[name])
