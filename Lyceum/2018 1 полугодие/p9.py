n = int(input())
c = "1 "
if n % 2 == 0:
    c = c + "2 "
if n % 3 == 0:
    c = c + "3 "
if n % 4 == 0:
    c = c + "4 "
if n % 5 == 0:
    c = c + "5 "
if n % 6 == 0:
    c = c + "6 "
if n % 7 == 0:
    c = c + "7 "
if n % 8 == 0:
    c = c + "8 "
if n % 9 == 0:
    c = c + "9 "
g = str(n)
c = c + g
print(c)
if "9" in c:
    print("НЕТ")
elif "8" in c:
    print("НЕТ")
elif "7" in c:
    print("НЕТ")
elif "6" in c:
    print("НЕТ")
elif "5" in c:
    print("НЕТ")
elif "4" in c:
    print("НЕТ")
elif "3" in c:
    print("НЕТ")
elif "2" in c:
    print("НЕТ")
else:
    print("ПРОСТОЕ")


Написал прогу через циклы.
Посмотри. Разберись до конца как работает.
Если непонятно - лучше спроси чем просто сдай задачу

n = int(input())
prostoe = "true"
deliteli = "1"

for i in range(2, n - 1):
    if n % i == 0:
        deliteli = deliteli + " " + str(i)
        prostoe = "false"
        
deliteli = deliteli + " " + str(n)
print(deliteli)
if prostoe == "true":
    print("ПРОСТОЕ")
else:
    print("НЕТ")    

