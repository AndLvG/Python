a = input()
b = input()
g = ""
h = 0
j = 0
v = 0
c = 0
while g != "стоп":
    f = int(input())
    g = input()
    if g == "север":
        h = h + f
        p = h
        v = v + 1
    elif g == "юг":
        h = h - f
        p = j
        v = v + 1
    if g == "восток":
        j = j + f
        p = m
        v = v + 1
    elif g == "запад":
        j = j - f
        p = n
        v = v + 1
    if a == h and b == j and c == 0:
        c = c + p
print(c)

Ничего непонятно что ты выше написал
В скайп тебе скину картинку

x = int(input())
y = int(input())
if y > 0:
    print("север")
else:
    y = y * (-1) # чтобы отрицательное число стало положительным = количесвто шагов
    print("юг")
print(y)
if x > 0:
    print("восток")
else:
    x = x * (-1)
    print("запад")
print(x)    