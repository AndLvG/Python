import sys

spisok = list(filter(lambda x: x[1].lstrip().startswith('#'), list(enumerate(list(map(str.strip, sys.stdin))))))
for i in spisok:
    print('Line {}: {}'.format(i[0] + 1, i[1].strip().lstrip('#')))

# for index, line in enumerate(spisok):
#     if line.lstrip().startswith('#'):
#         print('Line {}: {}'.format(index + 1, line.strip().lstrip('#')))
# print(spisok)

# s = list(map(lambda x: x.strip().lstrip('#'), filter(lambda x, y: y.lstrip().startswith('#'), enumerate(spisok))))
#
# print(s)

# s2 = list(map(lambda x: .strip().lstrip('#'), spisok))
