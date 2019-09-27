n = int(input())
hod = 0
while n != 1:
    if n % 2 == 0:
        n /= 2
    elif n % 2 == 1:
        n -= 1
    hod += 1
print(hod)