table = [[el for el in input().split(',')] for i in range(int(input()))]

for i in range(int(input())):
    s = [int(x) for x in input().split(',')]
    print(table[s[0]][s[1]])
