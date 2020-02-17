import re

ENG = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
RUS = ["йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю", "фывапролджэё"]

passwd = input()


def check_len(p):
    assert len(p) > 8


def check_letters(p):
    if not re.search('[A-ZА-Я]', p):
        raise AssertionError
    if not re.search('[a-zа-я]', p):
        raise AssertionError


def check_number(p):
    if not re.search('[0-9]', p):
        raise AssertionError


def check_klawa(p):
    for i in range(0, len(p) - 2):
        for el in ENG:
            for y in range(len(el) - 2):
                if el[y] + el[y + 1] + el[y + 2] in p.lower():
                    raise AssertionError
        for el in RUS:
            for y in range(len(el) - 2):
                if el[y] + el[y + 1] + el[y + 2] in p.lower():
                    raise AssertionError


flag = True
for func in (check_len, check_letters, check_number, check_klawa):
    try:
        func(passwd)
    except AssertionError as a:
        flag = False

if flag:
    print('ok')
else:
    print('error')
