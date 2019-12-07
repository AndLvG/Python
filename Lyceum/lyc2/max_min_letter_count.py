with open('input.txt', 'rt', encoding="utf8") as f:
    data = f.read()
max_let = max(''.join(set(data)), key=lambda char: data.count(char))
min_let = min(''.join(set(data)), key=lambda char: data.count(char))

print(max_let)
print(data.count(max_let))
print(min_let)
print(data.count(min_let))


