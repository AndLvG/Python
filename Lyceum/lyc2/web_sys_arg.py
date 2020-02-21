import sys

try:
    filename = sys.argv[-1]
    ar = []
    for arg in sys.argv[1:-1]:
        ar.append(arg)

    with open(filename, 'rt') as file:
        data = file.read().split('\n')
        if '--sort' in ar:
            data = sorted(data)

        for i, el in enumerate(data):
            if '--num' in ar:
                print(i, el)
            else:
                print(el)

        if '--count' in ar:
            print(f'rows count: {len(data)}')

except Exception:
    print('ERROR')
