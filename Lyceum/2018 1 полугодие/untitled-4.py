def nok(a, b):
    c = a * b
    while a and b:
        if a > b:
            a %= b
        else:
            b %= a
    return (c / (a + b))

n = int(input())
verh1 = int(input())
niz1 = int(input())
verh_sum = verh1
for i in range(n-1):
    verh2 = int(input())
    niz2 = int(input())    
    verh_sum += verh2
    niz1 = nok(niz1, niz2)
    print(niz1)
print(verh_sum)