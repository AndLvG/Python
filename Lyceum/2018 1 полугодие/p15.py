 lenght = int(input()) 
width = int(input()) 
spisok = []
for i in range(lenght):
    spisok.append(input())
spisok2=[]
for i in spisok[::2]:
    spisok2.append(i[::2])
for i in spisok2:
    print(i)