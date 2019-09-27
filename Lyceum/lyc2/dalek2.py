from sys import stdin

dalek = 0
for el in stdin:
    flag = 0
    for el1 in el.split():
        el1 = el1.lower()
        if el1[:5] == "далек" and flag == 0:
            dalek += 1
            flag = 1

print(dalek)
