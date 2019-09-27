from sys import stdin

words = []
k = 0
for el in stdin:
    words = el.split()
    for w in words:
        if 'далек' in w.lower():
            k += 1

print(k)
