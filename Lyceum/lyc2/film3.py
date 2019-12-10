import sqlite3
a = input()
con = sqlite3.connect(a)
cur = con.cursor()
result = cur.execute("""SELECT distinct year FROM Films
    WHERE title like 'Х%'""").fetchall()

for elem in result:
    print(*elem)

con.close()