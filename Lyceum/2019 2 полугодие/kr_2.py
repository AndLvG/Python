def map2(data, key=lambda x: x * 2):
    new = []
    for el in data:
        new.append(list(map(key, el)))
    return new

data = [[1], [2, 3], [4, 5, 6]]
res = map2(data)
print(res)