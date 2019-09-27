from itertools import permutations

dictionary = input().lower().split()
print(dictionary)

text = input().split()
print(text)

result = []

for el in text:
    flag = False
    for item in permutations(el):
        if ''.join(item).lower() in dictionary and ''.join(item).lower() != el.lower():
            result.append("#" * len(el))
            flag = True
            break
    if flag is False:
        result.append(el.lower())

print(*result)
