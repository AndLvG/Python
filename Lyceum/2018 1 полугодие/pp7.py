N = int(input())
пути = []
for i in range(N):
    while True:
        путь = input()
        if len([i for i in list(путь) if
                46 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or ord(i) == 95
                or 97 <= ord(i) <= 122]) == len(путь):
            пути.append(путь)
            break
M = int(input())
запросы = []
for i in range(M):
    while True:
        запрос = input()
        if len([i for i in list(запрос) if
                46 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or
                ord(i) == 95 or 97 <= ord(i) <= 122]) == len(запрос):
            запросы.append(запрос)
            break
for запрос in запросы:
    if len([0 for путь in пути if запрос.startswith(путь + '/')]) > 0:
        print('YES')
    else:
        print('NO')
