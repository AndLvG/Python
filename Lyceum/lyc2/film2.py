import sqlite3

a = input()  # + ".db"

con = sqlite3.connect(a)
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films
    WHERE title like '%?'""").fetchall()
for elem in result:
    print(*elem)

con.close()
