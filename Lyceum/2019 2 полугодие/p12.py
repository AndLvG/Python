def traspos(ar):
    return [[ar[row][col] for row in range(0, 4)] for col in range(0, 4)]


def horisont_otr(ar):
    return [[ar[col][row] for row in range(3, -1, -1)] for col in range(0, 4)]


def vertik_otr(ar):
    return [[ar[col][row] for row in range(0, 4)] for col in range(3, -1, -1)]


def sea_battle(ar):
    print("исходное поле")
    print(*ar, sep='\n')

    print("транспонирование")
    print(*traspos(ar), sep='\n')

    print("горизонтальное отражение")
    print(*horisont_otr(ar), sep='\n')

    print("вертикальное отражение")
    print(*vertik_otr(ar), sep='\n')

    print("отражение вдоль горизонтали и вертикали одновременно")
    print(*vertik_otr(horisont_otr(ar)), sep='\n')

    print("горизонтальное отражение, затем транспонирование")
    print(*traspos(horisont_otr(ar)), sep='\n')


sea_battle([['*', '*', '*', ' '],
            [' ', ' ', ' ', ' '],
            ['*', ' ', '*', '*'],
            ['*', ' ', ' ', ' ']])
