import sqlite3

a = input()  # + ".db"
con = sqlite3.connect(a)
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films 
    WHERE genre in (
SELECT id FROM genres 
    WHERE title = "музыка" Or title == "анимация") And year >= 1997""").fetchall()
for elem in result:
    print(*elem)

con.close()