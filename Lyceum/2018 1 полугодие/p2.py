n = int(input())
# Проверяем конечность дроби
# Раскладываем знаменатель на множители и если там присутствуют множители, отличные от 2 и 5 - дробь будет бесконечной
Mnozh = []
d = 2
while d * d <= n:
    if n % d == 0:
        Mnozh.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    Mnozh.append(n)
# Делаем множество из множителей и вычитаем из него множество 2,5
a = set(Mnozh)
b = {2, 5}
c = a.difference(b)
# Если в "с" ничего нет значит в множителях только 2 и 5
# И значит дробь будет конечной и в ответ нужно писать 0

chislitel = 1
otvet = ""
spisok = {}
index = 0
chislitel = chislitel % n
spisok[chislitel] = index
t = False
while not t:
    digit = chislitel * 10 // n  # Берём каждую цифру после запятой умножая chislitel каждый раз на 10
    chislitel = chislitel * 10 - (chislitel * 10 // n) * n
    if chislitel not in spisok:  # Пока числителя нет в списке - период дроби не закончился
        otvet += str(digit)  # добавляем в ответ цифру после запятой
        index += 1
        spisok[chislitel] = index
        t = False
    else:
        otvet += str(digit)
        t = True

if c:  # Если множество с множителями не пустое
    print(otvet)
else:
    print(0)
