import time

import schedule


def kuku():
    c = time.ctime()
    c = c.replace("  ", " ")
    c = c.split(" ")
    c = int(c[3].split(":")[0])
    if c > 11:
        c -= 12
    for el in range(c + 1):
        print("Ку", end="")
    print("Ку")


schedule.every(5).seconds.do(kuku)
while True:
    schedule.run_pending()
    time.sleep(1)