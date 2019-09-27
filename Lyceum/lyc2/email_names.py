list_mail = [input() for _ in range(int(input()))]

for _ in range(int(input())):
    number = 1
    name = input()
    mail = f'{name}@untitled.py'
    while mail in list_mail:
        mail = f'{name}{number}@untitled.py'
        number += 1
    print(mail)
