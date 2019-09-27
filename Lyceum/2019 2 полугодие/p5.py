def tic_tac_toe(field):
    WINS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    sfield = ""
    for i in range(3):
        sfield += "".join(field[i])
    win_exist = False
    for win in WINS:
        if sfield[win[0]] == sfield[win[1]] == sfield[win[2]] != '.':
            print('{0} win'.format(sfield[win[0]]))
            win_exist = True
            break
    if not win_exist:
        print('draw')


data = """0 - 0
x x x
0 0 -"""

field = [line.split() for line in data.split('\n')]

tic_tac_toe(field)
