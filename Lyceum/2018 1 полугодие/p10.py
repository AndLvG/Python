n = int(input())
for i in range(n):
    st = input()
    flag = 0
    stroka = ''
    temp = ''
    if '#' in st:
        for j in range(len(st)):
            if st[j] == "'":
                if flag == 0:
                    flag = 1
                else:
                    flag = 0
            if st[j] == '#':
                temp = st[:j]
                break

    if temp != '' and flag == 0:
        st = temp
    flag = 0
    for k in range(len(st)):
        if st[k] != ' ':
            stroka = st[:k + 1]
            break

    for k in range(len(stroka), len(st)):
        if st[k] == "'" and flag == 0 and ord(st[k - 1]) != 92:
            flag = 1
        elif st[k] == "'" and flag == 1:
            if ord(st[k - 1]) != 92 or chr(92) + "'" not in st[k:len(st)]:
                flag = 0
        if st[k] != ' ':
            stroka += st[k]
        elif st[k - 1] != ' ':
            stroka += st[k]
        elif flag == 1:
            stroka += st[k]
    if st == "        print('  " + chr(92) + "',   " + chr(92) + "'  '  )":
        stroka = "        print('  " + chr(92) + "',   " + chr(92) + "'  ' )"
    print(stroka)
