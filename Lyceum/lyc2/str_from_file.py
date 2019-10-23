import random

f = open("lines.txt", encoding="utf8")
lines = f.readlines()
ind = random.randint(0, len(lines))
print(lines[ind])
