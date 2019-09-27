
n = int(input())
b = 1
a = 0
while b * 2 * 2 < n:
    b = b * 2
    a = a + 1
b = b + 1
a = a + 1
b = b * 2
a = a + 1
while b < n:
    b = b + 1
    a = a + 1
print(a)