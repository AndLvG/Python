from sys import stdin

dat = []

for x in stdin:
    dat.append(x.replace('\n', '').split('\t'))

ceni = dat[1:]
print(ceni)

select = min(ceni, key=lambda x: sum(map(int, x[1:])))
print(select)

zagolovok = dat[0]
print(zagolovok)
print(list(zip(zagolovok, select)))

res = map(lambda x: f'{x[0]}\t{x[1]}'.strip(), zip(zagolovok, select))

print('\n'.join(res))

#     Арифметика для старших	Геометрия в четырехмерье	Эсперанто для начинающих
# Пятёрка	205	300	420
# Академкнига	500	200	250
# Всё для школы	350	350	350
