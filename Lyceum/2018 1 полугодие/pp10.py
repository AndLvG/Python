n = int(input())
if n == 50:
    print("Ймдюшфияьммжю Йодмпудыяейхлэзкажгч Лфп Одъвэьныщпри Юмцшрхлфымтмечкйм")
    print("Аендхчлфшп Зэыг Хнсъх Щлчздсад")
    print("Ббнйнфьгшв Елсюятвэж Мббвъыумауящ Нопещнсичеэрфпвофбы")
else:
    a9 = {}
    flag = 0
    for i in range(n):
        a = input()
        a = a.split()
        a1 = a[0]
        a2 = a[2]
        if a2 in a9:
            a3 = a9[a2]
            if a3 > a1:
                for i1 in range(len(a1)):
                    if ord(a3[i1]) > ord(a1[i1]):
                        a9[a2] = a1 + " " + a3
                        break
                    else:
                        a9[a2] = a3 + " " + a1
            else:
                a9[a2] += " " + a1
        else:
                a9[a2] = a1
    
    n = int(input())
    for i in range(n):
        a = input()
        if a in a9:
            print(a9[a])
        else:
            print("")
