file = open("prices.txt", encoding="utf8").readlines()
itogo = 0
for line in file:
    zapis = line.replace('\n', '').split("\t")
    itogo += int(zapis[1]) * float(zapis[2])
print(str(itogo))
