import csv

data = input().split()

with open("rez.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    title = next(reader)
    filt = list(filter(lambda x: x[1].split()[1] == data[0] and x[1].split()[2] == data[1], reader))

spisok = {}
for row in filt:
    spisok[row[1].split()[3]] = int(row[7])
sorted_spisok = sorted(spisok.items(), key=lambda x: (x[1], x[0]), reverse=True)
for el in sorted_spisok:
    print(el[0], el[1])
