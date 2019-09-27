transformation = lambda x: x

values = [1, 23, 42, "asdfg"]
transformed_values = list(map(transformation, values))
print(transformed_values)
if values == transformed_values:
    print('ok')
else:
    print('fail')
