from math import ceil
from sys import stdin

popul = {}

for x in stdin:
    city, _, pop = x.split()
    pop = int(ceil(int(pop) / 100000)) * 100  # Функция ceil окргуляет число в большую сторону
    popul[pop] = popul.get(pop, []) + [city]

popul = sorted(popul.items())

for k, v in popul:
    print('{} - {}: {}'.format(int(k) - 100, k, ', '.join(sorted(v))))
