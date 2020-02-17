import re

ENG = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
RUS = ["йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю", "фывапролджэё"]

passwd = input()


def check_len(p):
    return len(p) > 8


def check_letters(p):
    return re.search('[A-ZА-Я]', p) and re.search('[a-zа-я]', p)


def check_number(p):
    return re.search('[0-9]', p)


def check_klawa(p):
    for i in range(0, len(p) - 2):
        for el in ENG:
            for y in range(len(el) - 2):
                if el[y] + el[y + 1] + el[y + 2] in p.lower():
                    return False
        for el in RUS:
            for y in range(len(el) - 2):
                if el[y] + el[y + 1] + el[y + 2] in p.lower():
                    return False
    return True


if check_len(passwd) and check_letters(passwd) and check_number(passwd) and check_klawa(passwd):
    print('ok')
else:
    print('error')
