from random import choice
from sys import stdin


a1 = list(map(str.rstrip, stdin))
a2 = a1.copy()
for el in a1:
    a3 = choice(a2)
    if a3 == el:
        while a3 == el:
            a3 = choice(a2)
        a2.remove(a3)
        print(a3, "-", el)
    else:
        a2.remove(a3)
        print(a3, "-", el)
