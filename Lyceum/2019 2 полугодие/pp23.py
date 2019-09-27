import sys

spisok = list(map(str.strip, sys.stdin))

print(spisok)

print(*sorted(spisok, key=lambda x: sum([ord(i) - ord('A') + 1 for i in x.upper()])), sep='\n')
