from sys import stdin

number = int(input())
numbers = []

for line in stdin:
    line = list(map(int, line.split()))
    filt = list(filter(lambda x: x % number == 0, line))
    if len(filt) != 0:
        print(int(max(filt) - min(filt)))
    else:
        print(-1)
