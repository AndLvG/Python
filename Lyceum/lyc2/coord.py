cords = []
for el in range(int(input())):
    cords.append(list(map(int, input().split())))

print(cords)

left = [0, 0]
right = [0, 0]
top = [0, 0]
bottom = [0, 0]

for el in cords:
    if el[0] != 0 and el[1] != 0:
        if abs(el[1]) < abs(el[0]):
            print(f'({el[0]}, {el[1]})')
    if el[0] < left[0]:
        left = el
    if el[0] > right[0]:
        right = el
    if el[1] < bottom[1]:
        bottom = el
    if el[1] > top[1]:
        top = el

print(f'left: ({left[0]}, {left[1]})')
print(f'right: ({right[0]}, {right[1]})')
print(f'top: ({top[0]}, {top[1]})')
print(f'bottom: ({bottom[0]}, {bottom[1]})')
