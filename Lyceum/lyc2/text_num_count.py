with open('input.txt', 'rt') as f:
    data = f.read()
    print(data)
    data = data.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
    numbers = list(map(int, data.split()))

    print('массив цифр')
    print(numbers)
    print()

    print('первый вариант через фильтр')

    positive = list(filter(lambda x: x > 0, numbers))
    negative = list(filter(lambda x: x < 0, numbers))
    zero = list(filter(lambda x: x == 0, numbers))

    print('Кол-во отрицательных = {}, кол-во положительных = {}, кол-во нулей = {}'.format(len(negative), len(positive),
                                                                                           len(zero)))

    print()

    print('второй вариант чере sum')

    print('positive', sum(i > 0 for i in numbers))
    print('negative', sum(i < 0 for i in numbers))
    print('zero', sum(i == 0 for i in numbers))

with open('output.txt', 'wt') as f:
    f.write(str(len(data)) + '\n')
    str = ''
    if len(positive) > 0:
        str += f'1 {len(positive)}'
    if len(negative) > 0:
        str += f' -1 {len(negative)}'
    if len(zero) > 0:
        str += f' 0 {len(zero)}'
    f.write(str)
