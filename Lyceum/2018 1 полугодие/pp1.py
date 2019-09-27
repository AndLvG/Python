n = int(input())
for i in range(n):
    st = input()
    flag = 0
    stroka = ''
    temp = ''
    if '#' in st:
        for j in range(len(st)):
            if st[j] == '#':
                temp = st[:j]
                break

    if "'" not in temp and temp != '':
        st = temp

    for k in range(len(st)):
        if st[k] != ' ':
            stroka = st[:k + 1]
            break

    for k in range(1, len(st)):
        if st[k] == "'" and flag == 0:
            flag = 1
        elif st[k] == "'" and flag == 1:
            flag = 0
        if st[k] != ' ':
            stroka += st[k]
        elif st[k - 1] != ' ':
            stroka += st[k]
        elif flag == 1:
            stroka += st[k]
    print(stroka)
